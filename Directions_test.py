 
import requests
import json

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "appKey": "0BeLxmPc2W5oaSlKBNJsm5bIToGiFaSq7x8vhu7Y"
}

route_url = "https://apis.openapi.sk.com/transit/routes"

payload = {
    "startX": "127.02796290",
    "startY": "37.49807415",
    "endX": "126.972559",
    "endY": "37.554678",
    "format": "json",
    "count": 1
}

# POST 메서드로 요청해야 합니다.
route_response = requests.post(route_url, headers=headers, json=payload)
route_data = route_response.json()

print(json.dumps(route_data, ensure_ascii=False, indent=4))

 