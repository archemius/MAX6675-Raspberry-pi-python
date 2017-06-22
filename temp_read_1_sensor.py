# before import the max6675, you must save the max6675.py file at "/usr/lib/python2.7/dist-packages"

# wiring
# Raspberry         MAX6675
#       GND   ------   GND
#        5V     ------   VCC
#   pin 18     ------   SCK
#   pin 22     ------   CS
#   pin 16     ------   SO

# import max6675 module.
import max6675

# set the pin for communicate with MAX6675
cs = 22
sck = 18
so = 16

# max6675.set_pin(CS, SCK, SO, unit)   [unit : 0 - raw, 1 - Celsius, 2 - Fahrenheit]
max6675.set_pin(cs, sck, so, 1)

try:
    while 1:
        # read temperature connected at CS 22
        a = max6675.read_temp(cs)

        # print temperature
        print a

        # when there are some errors with sensor, it return "-" sign and CS pin number
        # in this case it returns "-22" 
        
        max6675.time.sleep(2)
        
except KeyboardInterrupt:
    pass



