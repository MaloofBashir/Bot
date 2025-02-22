import requests
import time

URL = "https://collegedext.onrender.com/"

while True:
    try:
        response = requests.get(URL)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(600)  # Wait for 10 minutes
