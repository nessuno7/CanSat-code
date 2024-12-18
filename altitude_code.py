import digitalio
import board
import time
#import radio
import bmp280
led = digitalio.DigitalInOut(board.LED)
while True:
    altitude = bmp280.read_altitude()
    message = "team ardingly rockets altitude is" + str(altitude)
    print(altitude)
    time.sleep(1)
