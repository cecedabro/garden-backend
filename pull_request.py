
import requests
print(requests.get("https://garden-backend-bhti.onrender.com/api/weather/latest").json())