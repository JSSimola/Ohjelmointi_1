#Sovellettu versio omasta moduuli 4 T3 (Min_Max.py) vastauksesta

num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input != "":
        num_list.append(int(user_input))
        continue
    else:
        break

num_list.sort(reverse=True)

print(num_list[0:5])
