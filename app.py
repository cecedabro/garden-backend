from flask import Flask, request, jsonify

app = Flask(__name__)

#Temporary mock database
weather_data = []

@app.route("/")
def hello():
    return "Hello, Garden! and is this working?"

@app.route("/api/weather", methods=["POST"])
def receive_weather():
    data = request.get_json()
    weather_data.append(data)
    return jsonify({"message": "Data recieved"}), 201

@app.route("/api/weather/latest", methods=["GET"])
def latest_weather():
    if weather_data:
        return jsonify(weather_data[-1])
    else:
        return jsonify({"message": "No data yet"}), 200
    
if __name__ == "__main__":
    app.run(debug=True)