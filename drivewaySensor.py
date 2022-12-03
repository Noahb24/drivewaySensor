from gpiozero import LED, Button
from signal import pause
import requests
import time

print ('Driveway Sensor is starting')

button = Button(4, pull_up=False)

triggered = False

def triggerSensor(state):
    if not state:
        x = requests.post('http://192.168.0.178:3500/driveway/tripped')
        print('Drive tripped')

while True:
    if button.is_pressed:
	print('closed')
	triggerSensor(triggered)
	triggered = True
    else:
	triggered = False
    time.sleep(0.5)

