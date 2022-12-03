from gpiozero import LED, Button
from signal import pause
import requests

print ('Driveway Sensor is starting')

button = Button(18)

def triggerSensor():
    x = requests.post('http://192.168.0.178:3500/driveway/tripped')
    print(x.text)
    print('Drive tripped')

button.when_pressed = triggerSensor

pause()
