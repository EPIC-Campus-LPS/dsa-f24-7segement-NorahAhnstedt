import RPi.GPIO as GPIO
import time
import tm1637
from datetime import datetime

GPIO.setmode(GPIO.BCM)
light = 20  #make sure you put it in gpio 20 or adjust this line
button = 19 #make sure you put putton in pin 13 or adjust this line
GPIO.setup(light, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Creating 4-digit 7-segment display object
tm = tm1637.TM1637(clk=5, dio=13)  # Using GPIO pins 18 and 17

clear = [0, 0, 0, 0]  # Defining values used to clear the display 
tm.write(clear) 
time.sleep(1)

states =[0, 1, 0] #0 -> LED off, 1 -> LED on 
i = 0 # state index 
t= 0000 #Time in seconds

def set_led_state(state):
    if state == 0:
        GPIO.output(light, GPIO.LOW)
    elif state == 1:
        GPIO.output(light, GPIO.HIGH)
    
def button_hold():
    while GPIO.input(button) == GPIO.LOW: #sleep for .1 secs to reset  
        time.sleep(0.1)

try:
    while True:
        button_state = GPIO.input(button)
        if button_state == GPIO.LOW:
            button_hold()
            i += 1
            if i >= len(states):
                i = 0 #reset state when it's cycled through the list
                t = 0000
            state = states[i]
            set_led_state(state)
        if states[i] == 1:  #trying to say while state = 1 and then break when i = 0 again but it might not work since state is alread established to be
            t += 1
            tm.numbers(0, t)
            time.sleep(1)
        else:
            tm.numbers(0, t)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

