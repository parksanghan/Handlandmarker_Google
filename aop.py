import requests

url = "https://maps.googleapis.com/maps/api/directions/json"

params = {
    'origin': '강남역',
    'destination': '서울역',
    'mode': 'transit',  # 대중교통 모드
    'language': 'ko',
    'key': '본인의_구글_API_키'
}

response = requests.get(url, params=params)
routes = response.json()

print(routes)