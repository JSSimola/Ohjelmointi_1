name_set = set()


while True:
    set_length = len(name_set)
    name_input = str(input("Anna nimi:"))
    if name_input == "":
        break
    name_set.add(name_input)
    if set_length == len(name_set):
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")

print("Annetut nimet:")
for n in name_set:
    print(n)
