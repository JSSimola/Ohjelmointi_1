import mysql.connector
from flask import Flask

app = Flask(__name__)
app.json.sort_keys = False

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='MariaDB',
         autocommit=True
         )

@app.route('/kenttä/<ICAO_Code>')
def getIcaoCode(ICAO_Code):
    query = "SELECT airport.name, airport.municipality FROM airport"
    query += " WHERE ident='" + ICAO_Code + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    vastaus = {
        "ICAO" : ICAO_Code,
        "Name": result[0][0],
        "Municipality" : result[0][1]
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
