# This is taken from the SparkFun Electronics on GitHub. Their  Qwiic_Joystick_Py repo had the following code example
# https://github.com/sparkfun/Qwiic_Joystick_Py

import qwiic_joystick
import time
import sys

def runExample():
    print("\nSparkFun qwiic Joystick Example 1 \n")
    myJoystick = qwiic_joystick.QwiicJoystick()
    
    if myJoystick.is_connected() == False:
        print("The Qwiic Joystick device isnt connected to the system", \
              file = sys.stderr)
        return
    myJoystick.begin()
    print ("Initialized. Firmware Version: %s" % myJoystick.get_version())
    
    while True:
        print("X: %d, Y: %d, Button: %d" % (myJoystick.get_horizontal(),
                                            myJoystick.get_vertical(),
                                            myJoystick.get_button()))
            
            
        time.sleep(0.8)
        

if __name__ == "__main__":
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)

