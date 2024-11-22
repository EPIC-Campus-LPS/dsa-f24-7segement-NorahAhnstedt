# Importing modules and classes
import tm1637
import time
from datetime import datetime


# Creating 4-digit 7-segment display object
tm = tm1637.TM1637(clk=5, dio=13)  # Using GPIO pins 18 and 17
clear = [0, 0, 0, 0]  # Defining values used to clear the display

# Displaying a rolling string
tm.write(clear)
time.sleep(1)

def user_input(): #creates function that promps user for name, captitalizes it and returns greeting
	name = input("")
	return f"Hello {name}" 


s = user_input() #this line calls user input functions assigning it to the vairable s
tm.scroll(s, delay=250) #prints s aka user input but with scrolling effect 
time.sleep(2)

tm.write(clear)
