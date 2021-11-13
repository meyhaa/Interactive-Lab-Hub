"""
	Reading distance from the laser based VL53L1X
	This example prints the distance to an object. If you are getting weird
	readings, be sure the vacuum tape has been removed from the sensor.
"""

import qwiic
import time

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")
	

previous_distance = 0
while True:
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(0.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(1)
		ToF.stop_ranging()
		if abs(previous_distance - distance) > 350:
            if (distance < 600):
                status = 'Out of bed'
            else:
                status = 'In bed'
            print('Client Status: ' + status)

		#print("Distance(mm): %s" % (distance))
		

	except Exception as e:
		print(e)
