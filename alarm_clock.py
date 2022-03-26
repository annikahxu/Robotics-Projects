from machine import Pin, I2C, PWM
from lcd1602 import LCD1602
import utime
from utime import sleep

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000) # Connect to I2C1 port
lcd = LCD1602(i2c, 2, 16) # read LCD1602 display

variableResistor = machine.ADC(0)
button = machine.ADC(1)
pwm = PWM(Pin(28))#DAC output (buzzer) connected to A1
value = variableResistor.read_u16() #value between ~304 to 65535 for resistor
pressed = button.read_u16()
val = 10000 #volume of alarm
    
move = False
#alarmOff = True
step = 0 #detects if button has been pressed
current_hour = 0
current_minute = 0
hour = 0
minute = 0
minuteset = 0


def select_hour():
    global value
    global hour
    lcd.home() # go to start
    lcd.clear() # clear
    lcd.print("SELECT HOUR:")
    lcd.setCursor(0, 1)
    hour = 24-int(round(value/2717))-1
    if hour == -1 or hour == 0:
        hour = 24
    lcd.print(str(hour))

def select_minute():
    global value
    global minute
    lcd.home()
    lcd.clear()
    lcd.print("SELECT MINUTE:")
    lcd.setCursor(0, 1)
    minute = 60-int(round(value/1087))-1
    if minute == -1 or minute == 60:
        minute = 0
    lcd.print(str(minute))

def print_time(hour1,minute1):
    lcd.home()
    lcd.clear()
    global hour
    global minute
    if minute1<10:
        lcd.print("TIME:"+str(hour1)+":"+"0"+str(minute1))
    else:
        lcd.print("TIME:"+str(hour1)+":"+str(minute1))
    lcd.setCursor(0, 1)
    if minute<10:
        lcd.print("ALARM:"+str(hour)+":"+"0"+str(minute))
    else:
        lcd.print("ALARM:"+str(hour)+":"+str(minute))

def chorus():
    global val
    pwm.freq(523)
    pwm.duty_u16(val)
    sleep(0.5)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(784)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(870)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(784)
    pwm.duty_u16(val)
    sleep(0.8)
    pwm.duty_u16(0)
    sleep(0.6)
    
    pwm.freq(698)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(659)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(587)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(523)
    pwm.duty_u16(val)
    sleep(0.8)
    pwm.duty_u16(0)
    sleep(0.6)
        
def verse():
    global val
    pwm.freq(784)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(698)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(659)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    pwm.duty_u16(val)
    sleep(0.4)
    pwm.duty_u16(0)
    sleep(0.4)
    
    pwm.freq(587)
    pwm.duty_u16(val)
    sleep(0.8)
    pwm.duty_u16(0)
    sleep(0.6)

def alarm():
    global value
    global val
    
#     pwm.freq(1000)
#     pwm.duty_u16(10000)
#     utime.sleep(0.5)
#     pwm.duty_u16(0)
#     utime.sleep(0.5)

    chorus()
    verse()
    verse()
    chorus()

while True:
    x = utime.localtime()
    current_hour = x[3]
    current_minute = x[4]
    
    move = False
    pressed = button.read_u16()
    value = variableResistor.read_u16()
    val = 10000-int(round(value/6.5))-1
    if val<0:
        val = 0
    
    if pressed == 65535:
        lcd.clear()
        step+=1
        
    #print(alarmOff)
    #print(step)
    
    if step<=0:
        print_time(current_hour, current_minute) 
        if current_hour == hour and current_minute == minute:
            chorus()
            verse()
            verse()
            chorus()
    if step>0 and step<=10:
        select_hour()
    if step>10 and step<=20:
        select_minute()
    if step>20:
        #alarmOff = False
        step = -10

