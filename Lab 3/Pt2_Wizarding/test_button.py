# This was taken from SparkFun Electronics on Github from their Qwiic_Button_Py repo. 
# This combines two of their examples: qwiic_button_ex1_buttonPress.py and qwiic_button_ex2_LEDon.py
# https://github.com/sparkfun/Qwiic_Button_Py/tree/main/examples

import qwiic_button 
import time
import sys

brightness = 50

def run_example():

    print("\nSparkFun Qwiic Button Example 1")
    my_button = qwiic_button.QwiicButton()

    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    print("\nButton ready!")
    
    while True:   
        
        if my_button.is_button_pressed() == True:
            print("\nThe button is pressed!")
            my_button.LED_on(brightness)

        else:
            my_button.LED_off()
            
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)





