from pyfirmata import Arduino, util
import time

arduino=Arduino('/dev/cu.usbmodem411')

ardui_pin=util.Iterator(arduino)
ardui_pin.start()


time.sleep(1)
motor=arduino.get_pin('d:9:s')
time.sleep(1)


def main():
	while 1: 
		motor.write(10)
		time.sleep(1)
		motor.write(270)
		time.sleep(1)

main()
