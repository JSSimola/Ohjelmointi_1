num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input != "":
        num_list.append(int(user_input))
        continue
    else:
        break

print("Pienin luku: " + str(min(num_list)))
print("Suurin luku: " + str(max(num_list)))
