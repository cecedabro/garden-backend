import requests
import random
import time

API_URL = "https://garden-backend-bhti.onrender.com/api/weather"

#Random data generator
while True:
    data = {
        "temperature": round(random.uniform(15, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "wind_speed": round(random.uniform(0, 10), 2)
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 201:
            print("Data sent", data)
        else:
            print("Error", response.status_code, response.text)
    except Exception as e:
        print("Failed to send data", e)
    
    time.sleep(10)


