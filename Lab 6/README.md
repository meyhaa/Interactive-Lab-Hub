# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

1. **A remote patient sensing and care system.** Takes inputs of info from sensors -- movement, a fall, light change, button input -- and alerts a caregiver who may be in another room, potentially managing multiple patients.

2. **Security and monitoring systems.** E.g. a baby monitor that takes in audio and video input and provides alerts and notifications to a caretaker who may be in another room.

3. **Tool to help manage plant care throughout a household.** Sensing water level, nitrogen/fertilizer, light level in the environment. Provides alerts to user for different plants in the space.

4. **Virtual charades/pictionary.** The user whose turn it is presses a button that tells the system it's their turn. The system only displays random prompts to that user. Button inputs could also be used to see who guesses first. A timer could keep all users synchronized.

5. **Virtual quiz game/trivia.** Capacitative sensors could be used for multiple choice style options. Who ever selects the correct option first wins that round. System identifies who the winner is based on timing of input for each round and the correct answer.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
<p float="left">
<img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/demo_twizzlers.png" height="350" />
</p>

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***


We chose to implement the accelerometer. See [accelerometer_sender.py](./accelerometer_sender.py)

<p float="left">
<img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/trial_accelerometer.png" height="350" />
</p>

### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

See [my_color.py](./my_color.py)
We added functionality to allow the user to specify the topic to subscribe/publish to. The default is to use IDD/colors.

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

We designed a remote patient sensing and monitoring tool that combines passive (multi-distance sensor) and active (capacitator) patient sensing to support caregivers in their work. The caregiver interface includes a screen display to indicate information about what is being sensed on the patient end, as well as interactive buttons that light up to indicate when a non-emergency or emergency request is made, and when pressed, allow the caregiver to indicate they have addressed the request.

Our application is focused on addressing scenarios where patients may have some level of mobility restriction and the caregiver may not be present in the same immediate space or room as the patient. For example, this could apply to overnight caregivers who need to be responsive to the patient's status overnight. The patient may wake up and need assistance getting out of bed and going to the bathroom, require water or medication, or even have an emergency situation. In this case, they can actively notify the caregiver they need assistance by using customized 'buttons' for their request that leverage the capacitator. The patient may attempt to get out of bed without notifying the caregiver. Depending on the patient's condition and fall risk, this could be dangerous. An alert based on distance sensor thresholds allows the caregiver to check in on the patient and see if they need assistance.

Communicating patient needs remotely allows the caregiver to respond more quickly and efficiently while also affording the patient some additional privacy. Furthermore, the system reduces the burden on the caregiver to be both physically bound to a particular location and constantly on alert (e.g. sitting by the patient's room, listening for changes) by visually notifying the caregiver when assistance is required. This could allow the caregiver to complete other tasks in a different location of the patient's home.

There is a growing body of literature on different algorithms that leverage state-of-the-art machine learning techniques or wearable sensors for bed monitoring. However, the majority of systems currently being used in facilities and care agencies require large sensors to be placed by the bed and output a loud alarm when triggered. Furthermore, these systems are also prone to false alarms which disturb the clients. Other systems use wearable sensors which have proven to be more accurate, but wearable systems do not as easily integrate into the lifestyles of users compared to embedded systems that do not require the user to wear or put on a device. Thus, although there have been recent technological advancements and new startups innovating in the space, there is still room for systems to be developed that focus on iterating on the design of the core interactions. With this project, we hope to apply the IDD framework to better explore this space and focus on designing the interactions.


**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

<p float="left">
  <img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/Lab6_Design.png" height="550" />
</p>

**Feature 1: Out of Bed Detection**

- Input: The Qwiic Multi Distance Sensor is placed on the user’s bed frame. 

- Computation: When the user gets out of bed, the distance from the sensor to closet reduces as the user’s feet is in between.  In turn Raspberry Pi 1 publishes a message to MQTT: “Out of Bed”.

- Output: Raspberry Pi 2 reads the MQTT value and displays a message in the Adafruit Mini PiTFT to help the client and the green LED in the Qwiic button is turned on. 

- Other interaction: If the light is turned on and then the green LED Qwiic button is pressed, the green light is turned off. This is for the caregiver to indicate they have checked in with the client. 

**Feature 2: Buttons for Different Requests**

- Input: In the cardboard UI prototype, there are small buttons made out of copper foil tape and connected to the 12-key capacitive touch sensor by alligator clips.

- Computation: When the user presses one of these buttons, Raspberry Pi 3 publishes messages to MQTT with the corresponding request (ie water). 

- Output: Raspberry Pi 2 reads the MQTT value and displays a message with the specific request in the Adafruit Mini PiTFT and the green LED in the Qwiic button is turned on. 

- Other interaction: If the light is turned on and then the green LED Qwiic button is pressed, the green light is turned off. This is for the caregiver to provide indicate they have taken care of the task. 

**Feature 3: Emergency Situation**

- Input: In the cardboard UI prototype, there is a singular large button made out of copper foil tape and connected to the 12-key capacitive touch sensor by alligator clips.

- Computation: When the user presses the large “Emergency” buttons, Raspberry Pi 3 publishes an emergency messages to MQTT.

- Output:  Raspberry Pi 2 reads the MQTT value and displays an emergency message in the Adafruit Mini PiTFT and the red LED in the Qwiic button is turned on. 

- Other interaction: If the light is turned on and then the red LED Qwiic button is pressed, the red light is turned off. This is for the caregiver to indicate they have checked in on the safety and wellbeing of the client. 


**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

We incorporated the three features (as described above) into the working prototype of our remote patient sensing monitoring system. As our system is specifically designed to bridge the gap between patient and caregiver, we implemented both patient-facing and caregiver-facing interfaces into our prototype. See [final_code folder](./final_code).

As described above, we designed a patient-facing sensing environment that collects inputs from the patient and relays them to the care team. One particular interface (please see below) consists of a cardboard UI prototype that allows patients to relay their needs to the care team at a press of a button. The prototype contains 6 labeled buttons corresponding to common patient needs. When a button is pressed, the specific request is relayed to a care team member who can then efficiently respond to the request. Also included in the UI prototype is a larger 7th button labeled 'Emergency'. In the event that a patient requires urgent attention, they may press this button which will send an SOS request to the care team.

<p float="left">
  <img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/cardboard_ui_prototype.png" height="450" />
</p>

We also utilized a distance sensor to implement out-of-bed detection capabilities that relays an alert to the care team when a patient has moved from their bed. The distance sensor is conspicuously placed and only requires a user to get out of bed to activate. 

<p float="left">
    <img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/out_of_bed_detection_setup.png" height="450" />
</p>

The caregiver-facing interface is a centralized system that continuously monitors the patient and relays outputs to the care team. When a patient submits a request through the patient-facing interface, the caregiver is alerted in two ways. First, an alert pops up on a screen that displays what the request was, and a green or red LED lights up depending on the nature of the request (green - general requests, red - SOS). Once the caregiver has responded to the request, they can come back and press the corresponding LED button to signal that the request(s) have been answered, at which point the LED light turns off. We believe requiring the caregiver to consciously input when requests have been completed will ensure that patient requests do not go unnoticed. In a similar way, the caregiver will bo notified on the screen when a patient has gotten out of bed. 

<p float="left">
  <img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/caregiver-interface.jpg" height="450" />
</p>

Please see the videos below for both a video based description of our prototype as well as a video of the prototype in action. 

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

The following 3 videos explain how our remote patient monitoring system enables effective communication between patients and caregivers

Out-of-bed detection: https://drive.google.com/file/d/1npoHy9gu62fRfPHu4zFFH5RJ68j2SCbB/view?usp=sharing

Cardboard UI Prototype for Patient Requests: https://drive.google.com/file/d/1E--pV_5cNh3vA555G9R6MHc_kum3ucaA/view?usp=sharing

How requests are relayed from patient to caregiver: https://drive.google.com/file/d/1maOZJk_9knsN3TTetw95zCp5RNV9wX44/view?usp=sharing

These 3 videos demonstrate our prototype in action, showcasing improved effectiveness of caregiver response to patient needs and requests:

Patient out-of-bed example: https://drive.google.com/file/d/1rcQD-gEz8ysPhYduCL9qxLKbQT172YYB/view?usp=sharing

Patient SOS example: https://drive.google.com/file/d/1IVk1-GZMK5CLcQODt3C4wo8cfF9EuivQ/view?usp=sharing

Patient medication request example: https://drive.google.com/file/d/1IVk1-GZMK5CLcQODt3C4wo8cfF9EuivQ/view?usp=sharing

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

