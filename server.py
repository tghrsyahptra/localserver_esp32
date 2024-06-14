from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Temporary list to store sensor data
sensor_data_list = []

@app.route('/sensor/data', methods=['POST'])
def post_sensor_data():
    data = request.json
    temperature = data.get('temperature')
    kelembapan = data.get('kelembapan')
    timestamp = datetime.now().isoformat()

    sensor_data = {
        'temperature': temperature,
        'kelembapan': kelembapan,
        'timestamp': timestamp
    }

    sensor_data_list.append(sensor_data)

    return jsonify({'message': 'Data successfully saved'}), 200

@app.route('/sensor/data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data_list), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
