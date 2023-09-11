import math

pizza_1 = []

user_pizza_1_size = float(input("Pizza 1 halkaisija(cm): "))
user_pizza_1_price = float(input("Pizza 1 hinta(€): "))

pizza_1.append(user_pizza_1_size)
pizza_1.append(user_pizza_1_price)

pizza_2 = []

user_pizza_2_size = float(input("Pizza 2 halkaisija(cm): "))
user_pizza_2_price = float(input("Pizza 2 hinta(€): "))

pizza_2.append(user_pizza_2_size)
pizza_2.append(user_pizza_2_price)

#print(pizza_1)
#print(pizza_2)


def pizza_calc(params):
    radius = params[0]/2
    radius_m = radius/100
    area = math.pi * (radius_m**2)
    unit_price = params[1] / area
    return unit_price

print(f"Pizza 1:n yksikköhinta (€ per m^2): {pizza_calc(pizza_1):0.1f}")
print(f"Pizza 2:n yksikköhinta (€ per m^2): {pizza_calc(pizza_2):0.1f}")

if pizza_calc(pizza_1) < pizza_calc(pizza_2):
    print("Pizza 1 antaa paremman vastineen rahalle")
else:
    print("Pizza 2 antaa paremman vastineen rahalle")
