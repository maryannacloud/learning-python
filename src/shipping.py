class ShippingCalculator:

    @staticmethod
    def calculate_ground_shipping_cost(weight):
        ground_shipping_flat_charge = 20
        if weight <= 2:
          price_per_lb_ground = 1.5
        elif 2 < weight <= 6:
          price_per_lb_ground = 3
        elif 6 < weight <= 10:
          price_per_lb_ground = 4
        elif weight > 10:
          price_per_lb_ground = 4.75

        total_cost = weight * price_per_lb_ground + ground_shipping_flat_charge
        return total_cost, price_per_lb_ground, ground_shipping_flat_charge

    @staticmethod
    def calculate_premium_shipping_cost():
        premium_shipping_flat_charge = 125
        return premium_shipping_flat_charge

    @staticmethod
    def calculate_drone_shipping_cost(weight):
        if weight <= 2:
          price_per_lb_drone = 4.5
        elif 2 < weight <= 6:
          price_per_lb_drone = 9
        elif 6 < weight <= 10:
          price_per_lb_drone = 12
        elif weight > 10:
          price_per_lb_drone = 14.25

        total_cost = weight * price_per_lb_drone
        return total_cost, price_per_lb_drone


def calculate_lowest_shipping_cost(weight):
    ground_cost, _, _ = ShippingCalculator.calculate_ground_shipping_cost(weight)
    premium_cost = ShippingCalculator.calculate_premium_shipping_cost()
    drone_cost, _, = ShippingCalculator.calculate_drone_shipping_cost(weight)

    shipping_options = {
        "Ground Shipping": ground_cost,
        "Premium Ground Shipping": premium_cost,
        "Drone Shipping": drone_cost
    }

    best_method = min(shipping_options, key=shipping_options.get)
    lowest_cost = shipping_options[best_method]

    return lowest_cost, best_method