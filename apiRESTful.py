from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL base de la API MockAPI para IoTCarStatus
BASE_URL = 'https://66eb01e755ad32cda47b4edb.mockapi.io/IoTCarStatus'


# Leer todos los registros (GET)
@app.route('/cars', methods=['GET'])
def get_all_cars():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Error fetching cars'}), response.status_code


# Leer un registro específico por ID (GET)
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car_by_id(car_id):
    response = requests.get(f'{BASE_URL}/{car_id}')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'Car with ID {car_id} not found'}), response.status_code


# Crear un nuevo registro (POST)
@app.route('/cars', methods=['POST'])
def create_car():
    new_car = request.json  # Datos del nuevo carro
    response = requests.post(BASE_URL, json=new_car)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({'error': 'Error creating car'}), response.status_code


# Actualizar un registro existente (PUT)
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    updated_car = request.json  # Datos para actualizar
    response = requests.put(f'{BASE_URL}/{car_id}', json=updated_car)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'Error updating car with ID {car_id}'}), response.status_code


# Eliminar un registro por ID (DELETE)
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    response = requests.delete(f'{BASE_URL}/{car_id}')
    if response.status_code == 200:
        return jsonify({'message': f'Car with ID {car_id} deleted successfully'}), 200
    else:
        return jsonify({'error': f'Error deleting car with ID {car_id}'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
