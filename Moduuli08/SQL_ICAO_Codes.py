import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='MariaDB',
         autocommit=True
         )

def getIcaoCode(ICAO_Code):
    query = "SELECT airport.name, airport.municipality FROM airport"
    query += " WHERE ident='" + ICAO_Code + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

ICAO_Code = input("Anna ICAO-koodi: ")
result = getIcaoCode(ICAO_Code)
print(result[0])
