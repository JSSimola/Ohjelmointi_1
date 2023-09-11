lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 111]

print("Alkuperäinen lista: "+ str(lista))

def odd_num_del(list):
    for i in list[:]:
        if i % 2 != 0:
            list.remove(i)
    return list

odd_num_del(lista)

print("Parittomat poistettu: "+str(lista))
