import time
import board
import busio
import adafruit_mpu6050

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/mb/accl'

i2c = busio.I2C(board.SCL, board.SDA)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    print("Temperature: %.2f C"%mpu.temperature)
    print("")
    time.sleep(5)
    val = "Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration)
    client.publish(topic, val)
    #for i in range(12):
     #   if mpr121[i].value:
      #      val = f"Twizzler {i} touched!"
       #     print(val)
        #    client.publish(topic, val)
    time.sleep(0.25)
