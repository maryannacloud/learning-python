# time_travelers_toolkit.py
import datetime as dt
from decimal import Decimal
from random import randint, choice

# Import from our custom module (must be in the same folder)
import custom_module

# -------------------------
# 1) Get today's date/time
# -------------------------
current_datetime = dt.datetime.now()
current_date_str = current_datetime.strftime("%Y-%m-%d")
current_time_str = current_datetime.strftime("%H:%M:%S")

print(f"Today's date is: {current_date_str}")
print(f"Current time is: {current_time_str}\n")

# -------------------------
# 2) Randomly pick a year
# -------------------------
try:
  target_year = randint(1900, 2050)
except ValueError:
  print("Error generating random year")

# -------------------------
# 3) Choose a random destination
# -------------------------
destinations = [
    "Ancient Rome",
    "the Wild West",
    "the Age of Dinosaurs",
    "the Renaissance",
    "the Mars Colony",
]
selected_destination = choice(destinations)

# -------------------------
# 4) Calculate travel cost
# -------------------------
# Base cost for time travel:
base_cost = Decimal("10.00")

# The multiplier is based on how far we're traveling from *this* year
year_difference = abs(current_datetime.year - target_year)
year_multiplier = Decimal(str(year_difference))

def calculate_travel_cost(base_cost, year_difference):
    year_multiplier = Decimal(str(year_difference))
    return base_cost + year_multiplier

final_cost = calculate_travel_cost(base_cost, year_difference)

# Format to two decimals, for example "$23.00"
formatted_cost = f"${final_cost:.2f}"

# -------------------------
# 5) Generate the message!
# -------------------------
message = custom_module.generate_time_travel_message(
    year = target_year,
    destination = selected_destination,
    cost = formatted_cost
)

print(message)
