import requests
BASE_URL = 'http://10.8.0.6:5000/'
response = requests.get(f"{BASE_URL}/")
print(response.text)
