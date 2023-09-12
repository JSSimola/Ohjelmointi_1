airports = dict()

while True:
    user_choice = str(input("Luo uusi lentoasema(=A), Lue lentoaseman nimi(=B) tai lopeta(=Q): "))
    if user_choice == "A":
        code = str(input("Anna ICAO-koodi: "))
        name = str(input("Anna lentoaseman nimi: "))
        airports[code] = name
    elif user_choice == "B":
        user_ask_code = str(input("Anna ICAO-koodi: "))
        if code in airports:
            print(airports[code])
    else:
        quit()
