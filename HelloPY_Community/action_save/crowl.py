import requests

url = 'https://www.youtube.com/playlist?list=PLZPhyNeJvHRllQiXsJAryqWmqWrwFxY8I'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("요청 실패", response.status_code)