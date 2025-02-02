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