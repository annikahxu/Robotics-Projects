from machine import Pin, I2C
from lcd1602 import LCD1602
import utime

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) # Connect to I2C1 port
lcd = LCD1602(i2c, 2, 16) # read LCD1602 display

variableResistor = machine.ADC(0)
button = machine.ADC(1)
list = ['apple', 'banana', 'cherry', 'kiwi', 'peach', 'mango', 'strawberry', 'raspberry', 'blueberry', 'guava', 'pineapple', 'lemon', 'grapefruit', 'blackberry', 'watermelon']
current = 0

while True:
    value = variableResistor.read_u16() #value between ~304 to 65535
    pressed = button.read_u16()
    #print(pressed)
    #print(value)
    #utime.sleep(0.2)
    #4349 is the interval between each value
    current = int(round(value/4349))-1
    if current == -1:
        current = 0
    lcd.home() # go to start
    lcd.clear() # clear
    lcd.print(str(list[current]))
    lcd.setCursor(0, 1)
    if current<(len(list)-1):
        lcd.print(str(list[current+1]))
    if pressed == 65535:
        print("selected:",list[current])