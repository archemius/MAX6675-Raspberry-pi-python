# before import the max6675, you must save the max6675.py file at "/usr/lib/python2.7/dist-packages"

# wiring
# Raspberry         first MAX6675       Raspberry    second MAX6675
#       GND   ------   GND                           GND   ------   GND
#        5V     ------   VCC                             5V     ------   VCC
#   pin 18     ------   SCK                       pin 18     ------   SCK
#   pin 22     ------   CS                         pin 29     ------   CS
#   pin 16     ------   SO                         pin 16     ------   SO

# import max6675 module.
import max6675

# in this case there are two sensor. one is connected to 22 with CS, the other is connected to 29 with CS
cs1 = 22
cs2 = 29
sck = 18
so = 16

# max6675.set_pin(CS, SCK, SO, unit)  [unit : 0 - raw, 1 - Celsius, 2 - Fahrenheit]
max6675.set_pin(cs1, sck, so, 1)
max6675.set_pin(cs2, sck, so, 1)

try:
    while 1:

        # read temperature connected at CS 22
        a = max6675.read_temp(cs1)

        # read temperature connected at CS 29
        b = max6675.read_temp(cs2)
        
        # print temperature connceted at CS 22
        print a
        # print temperature connceted at CS 29
        print b
        max6675.time.sleep(2)
        
except KeyboardInterrupt:
    pass



