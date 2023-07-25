from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'cars'
}

# Function to get car models from the database
def get_car_models():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT * FROM cars;"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

# Route for the GET method to fetch car model data
@app.route('/car_models', methods=['GET'])
def fetch_car_models():
    car_models = get_car_models()
    print(car_models)
    response = [{"id": model[0], "type": model[1], "color": model[2], "model": model[3]} for model in car_models]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
