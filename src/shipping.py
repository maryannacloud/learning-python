weight = 1.5

# Ground Shipping
ground_shipping_flat_charge = 20
if weight <= 2:
  price_per_lb_ground = 1.5
  ground_shipping_cost = weight * price_per_lb_ground + ground_shipping_flat_charge
elif 2 < weight <= 6:
  price_per_lb_ground = 3
  ground_shipping_cost = weight * price_per_lb_ground + ground_shipping_flat_charge
elif 6 < weight <= 10:
  price_per_lb_ground = 4
  ground_shipping_cost = weight * price_per_lb_ground + ground_shipping_flat_charge
elif weight > 10:
  price_per_lb_ground = 4.75
  ground_shipping_cost = weight * price_per_lb_ground + ground_shipping_flat_charge

print("With package weight of " + str(weight) + "lb and price per pound of $" + str(price_per_lb_ground) + ", your total cost via Ground Shipping is: $" + str(ground_shipping_cost) + ", which also includes a $" + str(ground_shipping_flat_charge) + " Ground Shipping Flat Charge.")
print("")

# Ground Shipping Premium
premium_shipping_flat_charge = 125
print("Ground Shipping Premium Flat charge is: $" + str(premium_shipping_flat_charge))
print("")

# Drone Shipping
if weight <= 2:
  price_per_lb_drone = 4.5
  drone_shipping_cost = weight * price_per_lb_drone
elif 2 < weight <= 6:
  price_per_lb_drone = 9
  drone_shipping_cost = weight * price_per_lb_drone
elif 6 < weight <= 10:
  price_per_lb_drone = 12
  drone_shipping_cost = weight * price_per_lb_drone
elif weight > 10:
  price_per_lb_drone = 14.25
  drone_shipping_cost = weight * price_per_lb_drone

print("With package weight of " + str(weight) + "lb and price per pound of $" + str(price_per_lb_drone) + ", your total cost via Drone Shipping is: $" + str(drone_shipping_cost))
print("")