city_list = []

for i in range(0, 5):
    user_input = input(str(i+1)+"/5"+" Anna kaupungin nimi: ")
    city_list.append(user_input)

for i in range(0, 5):
    print(city_list[i])
