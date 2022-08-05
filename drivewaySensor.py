from gpiozero import LED, Button
from signal import pause

print ('Driveway Sensor is starting')

button = Button(18)

def onButtonPressed():
    print('Drive tripped')

button.when_pressed = onButtonPressed

pause()