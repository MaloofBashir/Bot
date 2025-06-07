import requests
import time
import datetime

URL = "https://collegedext.onrender.com/"
print(f"Running at {datetime.datetime.utcnow()} UTC")

try:
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

# Sleep to simulate real work (GitHub might skip jobs if they’re too short)
time.sleep(60) 
