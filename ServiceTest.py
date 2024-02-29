import json, time

while True:
    f = open('move.json')
    move = json.load(f)
    print(move)
    time.sleep(1/60)
    f.close()