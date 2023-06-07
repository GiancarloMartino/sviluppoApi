import requests

url = "http://localhost:8000/users"
data = {
    "id": 1,
    "name": "John Marzu",
    "email": "john.marz@example.com"
}
response = requests.post(url, json=data)
print(response.json())





