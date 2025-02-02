from src.shipping import ShippingCalculator

def main():
    weight = 1.5

    shipping_calculator = ShippingCalculator()

    # Ground Shipping
    ground_cost, ground_price_per_lb, ground_flat_charge = shipping_calculator.calculate_ground_shipping_cost(weight)
    print(
        f"With package weight of {weight}lb and price per pound of ${ground_price_per_lb}, "
        f"your total cost via Ground Shipping is: ${ground_cost}, which also includes a "
        f"${ground_flat_charge} Ground Shipping Flat Charge."
    )
    print("")

    # Ground Shipping Premium
    premium_cost = shipping_calculator.calculate_premium_shipping_cost()
    print(f"Ground Shipping Premium Flat charge is: ${premium_cost}")
    print("")

    # Drone Shipping
    drone_cost, drone_price_per_lb = shipping_calculator.calculate_drone_shipping_cost(weight)
    print(
        f"With package weight of {weight}lb and price per pound of ${drone_price_per_lb}, "
        f"your total cost via Drone Shipping is: ${drone_cost}"
    )
    print("")

    lowest_cost, best_method = calculate_lowest_shipping_cost(weight)
    print(f"The cheapest shipping method for {weight}lb is {best_method} at a cost of ${lowest_cost:.2f}.")


if __name__ == "__main__":
    main()