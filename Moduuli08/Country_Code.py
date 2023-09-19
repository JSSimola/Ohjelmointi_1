import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='MariaDB',
         autocommit=True
         )

def getCountryCode(Country_Code):
    query = "SELECT airport.type, count(*) FROM airport"
    query += " WHERE iso_country='" + Country_Code + "'"
    query += " group by type"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

Country_Code = input("Anna maakoodi: ")
result = getCountryCode(Country_Code)
print(result)
