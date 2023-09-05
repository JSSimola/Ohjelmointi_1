gallons = 1
def volume_conversion(gallons):
    liters = gallons * 3.785
    return liters

while gallons >= 0:
    gallons = float(input("Anna gallonat: "))
    conv = volume_conversion(gallons)
    if gallons >= 0:
        print(f"Litroina: {conv:0.1f}")
    else:
        quit()
