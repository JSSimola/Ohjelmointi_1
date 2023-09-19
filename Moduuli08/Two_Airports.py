import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='MariaDB',
         autocommit=True
         )

def getAirportsLatLon(ICAO_Code):
    query = "SELECT latitude_deg, longitude_deg from airport"
    query += " WHERE ident='" + ICAO_Code + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

ICAO_Code_1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
airport_1 = getAirportsLatLon(ICAO_Code_1)

ICAO_Code_2 = input("Anna toisen lentokentän ICAO-koodi: ")
airport_2 = getAirportsLatLon(ICAO_Code_2)

ans_dist = distance.great_circle(airport_1, airport_2)
print(f"Kenttien välinen etäisyys on: {ans_dist}")
