import math

# Leiviskän käännös on talent?

talent = float(input("Anna leiviskät: "))
nails = float(input("Anna naulat: "))
bullets = float(input("Anna luodit: "))

# muunnetaan grammoiksi
mass_talent_g = talent * 20 * 32 * 13.3
mass_nails_g = nails * 32 * 13.3
mass_bullets_g = bullets * 13.3

mass_g = mass_talent_g + mass_nails_g + mass_bullets_g

# muunnetaan kilogrammoiksi
mass_kg = mass_g / 1000

# eritellään desimaalit luvusta
result = math.modf(mass_kg)
result_kg = result[1]
result_g = result[0]

result_g = result_g * 1000

print("Massa nykymittojen mukaan:")
print(f"{result_kg:1.0f} kilogrammaa ja {result_g:1.0f} grammaa.")
