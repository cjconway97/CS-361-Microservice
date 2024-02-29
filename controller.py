import keyboard
import json
import time

key = ''
while True:
    key = keyboard.read_key()
    if key == 'w' or key == 'up':
        with open("move.json", "w") as outfile:
            json.dump({'direction': 'up'}, outfile)
    elif key == 'd' or key == 'right':
        with open("move.json", "w") as outfile:
            json.dump({'direction': 'right'}, outfile)
    elif key == 'a' or key == 'left':
        with open("move.json", "w") as outfile:
            json.dump({'direction': 'left'}, outfile)
    elif key == 's' or key == 'down':
        with open("move.json", "w") as outfile:
            json.dump({'direction': 'down'}, outfile)
    time.sleep(1/15)
