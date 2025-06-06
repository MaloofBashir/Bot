import requests
import time


URL = "https://collegedext.onrender.com/"

try:
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
