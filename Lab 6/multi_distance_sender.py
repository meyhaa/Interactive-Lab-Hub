import time
import board
import digitalio
import busio
import sys
import qwiic_vl53l1x

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/mb/prox'

mySensor = qwiic_vl53l1x.QwiicVL53L1X()

if mySensor.isConnected() == False:
    print("The Qwiic VL53L1X device isn't connected to the system. Please check your connection", \
          file=sys.stderr)
    run_example = False
else:
    mySensor.sensor_init()
    run_example = True

while run_example:
    try:
        mySensor.start_ranging()  # Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance = mySensor.get_distance()  # Get the result of the measurement from the sensor
        time.sleep(.005)
        mySensor.stop_ranging()
        print("Distance(mm): %s" % distance)
    except Exception as e:
        print(e)

    #client.publish(topic, val)
    
    #time.sleep(0.25)
