# -------------------------------
# 1) Menu class
# -------------------------------
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # 2) String representation
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    # 3) calculate_bill
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total


# -------------------------------
# Create the four menus
# -------------------------------
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, "11am", "4pm")

early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}
early_bird = Menu("Early-bird", early_bird_items, "3pm", "6pm")

dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
}
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")

kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
kids = Menu("Kids", kids_items, "11am", "9pm")

# -------------------------------
# Test the string representation
# -------------------------------
# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)

# -------------------------------
# 4) Test calculate_bill()
# -------------------------------
brunch_order = ["pancakes", "home fries", "coffee"]
brunch_bill = brunch.calculate_bill(brunch_order)
# print(brunch_bill)  # Example: 7.50 + 4.50 + 1.50 = 13.50

early_bird_order = ["salumeria plate", "mushroom ravioli (vegan)"]
early_bird_bill = early_bird.calculate_bill(early_bird_order)


# print(early_bird_bill)  # Example: 8.00 + 13.50 = 21.50

# -------------------------------
# 5) Franchise class
# -------------------------------
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # 6) String representation
    def __repr__(self):
        return f"Franchise located at {self.address}"

    # 7) available_menus(time)
    def available_menus(self, time):
        # We need to interpret times as hours for a simpler comparison,
        # but for this project we can just do string logic or keep it conceptual.
        # We'll do a quick hack: convert "3pm" -> 15, "11am" -> 11, etc.

        # Convert something like "5pm" to an integer 17, "12pm" -> 12, "11am" -> 11, "12am" -> 0, etc.
        def time_to_24hr(time_str):
            # '11am' -> 11, '4pm' -> 16
            hour = int(time_str[:-2])  # everything but last two chars
            am_pm = time_str[-2:].lower()
            if am_pm == 'am':
                # 12am is 0 in 24-hour
                return hour % 12
            else:
                # for PM, we add 12 except for 12pm which is 12
                return (hour % 12) + 12

        time_24 = time_to_24hr(time)
        menus_available = []
        for menu in self.menus:
            start_24 = time_to_24hr(menu.start_time)
            end_24 = time_to_24hr(menu.end_time)
            # If time_24 is within [start_24, end_24), let's assume inclusive at start, exclusive at end
            if start_24 <= time_24 < end_24:
                menus_available.append(menu)
        return menus_available


# -------------------------------
# Create franchises
# -------------------------------
menus_all = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus_all)
new_installment = Franchise("12 East Mulberry Street", menus_all)


# -------------------------------
# Test available_menus
# -------------------------------
# noon_menus = flagship_store.available_menus("12pm")
# print(noon_menus)
# # Should see brunch and kids, since noon -> 12: 11am <=12 <4pm is brunch, 11am <=12 <9pm is kids

# five_pm_menus = new_installment.available_menus("5pm")
# print(five_pm_menus)
# # Should see dinner (5pm-11pm) and also kids menu (11am-9pm).

# -------------------------------
# 8) Business class
# -------------------------------
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f"Business: {self.name}"


# Create the first Business
basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# -------------------------------
# Create an arepas menu
# -------------------------------
arepas_items = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}
arepas_menu = Menu("Arepas", arepas_items, "10am", "8pm")

# Create our Take a' Arepa franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create our new Business
arepa_business = Business("Take a' Arepa", [arepas_place])

# -------------------------------
# Final test prints (optional)
# -------------------------------
print(basta_business)
print(arepa_business)
print(arepas_place)
print(arepas_place.available_menus("11am"))
