n_1 = int(input("Anna ensimmäinen kokonaisluku: "))
n_2 = int(input("Anna toinen kokonaisluku: "))
n_3 = int(input("Anna kolmas kokonaisluku: "))

sum = n_1 + n_2 + n_3
product = n_1 * n_2 * n_3
average = (n_1 + n_2 + n_3) / 3

print("Annettujen lukujen summa: " + str(sum))
print("Annettujen lukujen tulo: " + str(product))
print(f"Annettujen lukujen keskiarvo: {average:6.1f}")
