import requests, time

while True:
    move = requests.get('http://localhost:5001/nextmove')
    print(move.text)
    time.sleep(0.25)