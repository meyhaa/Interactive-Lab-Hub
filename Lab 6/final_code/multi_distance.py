"""
	Reading distance from the laser based VL53L1X
	This example prints the distance to an object. If you are getting weird
	readings, be sure the vacuum tape has been removed from the sensor.
	"""

import qwiic
import time


import paho.mqtt.client as mqtt
import uuid



client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/syw/multi-distance'


print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):	# Begin returns 0 on a good init
	print("Sensor online!\n")
	

previous_distance = 0
while True:
	try:
		ToF.start_ranging()	 # Write configuration bytes to initiate measurement
		time.sleep(0.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(1)
		ToF.stop_ranging()

		if abs(previous_distance - distance) > 450:
			if (distance < 1400):
				status = 'Out of bed'
			else:
				status = 'In bed'
			previous_distance = distance
			print('Client Status: ' + status)
			client.publish(topic, status)

		print("Distance(mm): %s" % (distance))
		
	except Exception as e:
		print(e)
