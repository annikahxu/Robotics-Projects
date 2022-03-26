from ws2812 import WS2812
from machine import I2C,Pin,ADC
import time
import os

WHITE = (255, 255, 255)

#WS2812(pin_num,led_count)
led = WS2812(18,30)
light = ADC(0)
led.pixels_set(0, WHITE)
led.pixels_show()

while True :
    distance = input("please type distance:")
    if 's'== distance:
        break
    else:
        lightVal = light.read_u16()
        print(lightVal)
        fp = open('calibration table', 'a')
        fp.write("distance = "+str(distance)+" , intensity of reflected light = "+str(lightVal)+'\n')
        fp.close()
        #os.remove("calibration table")



 

