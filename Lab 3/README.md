# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

My shell file is saved as GoogleTTS_Meyhaa_shell.sh in this repo. 

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

The "pt1_asking_questions.sh" shell file in this repo asks "How many hours did you sleep last night". 

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

For Part 1 of this lab, I chose to storyboard a voice based HW assistant. This HW assistant is activated by a study mode button on the Pi. Once activated, the HW assistant asks the user to verbally list out the tasks they hope to accomplish for the day along with the amount of time they want to study. Then, the Pi will follow the  Pomodoro Technique to guide the user to study in sessions of 25 min. After every 25 minute session, there will be a 5-10 min break. After 4 of these 25 minute sessions, there will be a longer ~30 min break. During each break, the HW assistant will check in about progress, conduct breathing exercises, or voice motivational messages.  

![Storyboard](https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%203/Lab3_Storyboard.png)

\*\***Please describe and document your process.**\*\*

I started out with this simple storyboard sketch. However, I felt I needed to better utilize post-its/cards to further communicate this voice assistant interactions. So, I updated my storyboard above by having two main components: a Pi on white colored paper and a person on purple colored paper. This allowed me to separate out the Pi and user dialogues more clearly. 
<p float="center">
<img src="https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%203/Lab3_old_V1_Storyboard.png" height="350" />
</p>


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

Video: 
[![Video with interaction](https://img.youtube.com/vi/ALPBCr2PMGg/maxresdefault.jpg)](https://youtu.be/ALPBCr2PMGg)

Admittedly, this was somewhat awkward to film. I used my brother as an actor. I need to work on my pretending to be a device skills. This was different than what I had imagined for a couple reasons:
- (1) Conveying time is difficult. A significant component of my device interaction is that the Pi checks in with the user in 25 min increments (as per the Pomodoro studying method). In storyboard form, it was easy to show the passage of time between panels with a text based indicator. However, over video, it was less natural to demonstrate time had passed. And I hadn’t thought of this before recording, so I did some awkward hand motions to signal the passage of 25 minutes. 

- (2) Tasks were interpreted differently. Starting with the first task, I had asked him to “List the tasks you hope to accomplish in this HW session and how long you will be studying”. I had storyboarded an example where the user responds with tasks XYZ and a X time that represents the total time of the study session. My brother answered the question by listing a task but then specifying how long he hoped to spend for each task. For example “algebra 2/trig for an hour and biology HW for an hour” VS  “algebra 2/trig and biology for a 2 hour total study session”

- (3) Dialogue was more open ended. My brother was talking to me (the device) like he would a friend. He was saying a joke, complaining about hw a little, etc. His answers were not as to the point or concise as per my initial storyboard. 

Overall, this was a really valuable exercise. In our storyboards, I focused too narrowly on one storyline and a set of potential responses. Even for such a simple watered down task with a handful of questions, there are so many potential variations and voice interactions. For next time, I hope to approach such video sessions more openly as a designer. In my responses back to my brother as the device, I was internally confused of what to say back because I was more focused on the technical limitations of what I COULD say back rather than focused on getting at the heart of the interaction. This was quite a rough and bare bones video, but it gave me a lot to think about when looking to design such an interaction. 

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

One of the main improvements is tweaking the wording to better anticipate potential misunderstandings. In the original storyboard, the Pi asks the user to list both (1) the tasks they intend to accomplish and (2) the length of time they intend to study. From the learnings with the pt.1 video, I will be breaking it up into two questions to limit the open-ended nature of the study session length question. 

Furthermore, I will also be adding additional wording for the Pi to explain what it does in the storyboard use case. From the video and feedback, it was clear that new users were a little confused as to what the purpose of the Pi StudyBot was. So including some background text would help alleviate such confusion. 


2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

Buttons can be used to (1) turn on study mode on the Pi and/or (2) indicate to the Pi that you are back from a study session. 


3. Make a new storyboard, diagram and/or script based on these reflections.
![Updated Storyboard](https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%203/Lab3_Pt2_updated_storyboard.png)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

Here are diagrams further outlining how participants will speak and interact with the device. Beyond the initial set up conversation from the storyboard, the other main interactions are during breaks. The Pi will communicate to the user when the 25 minute session is complete and indicate what type of break it is; short breaks are 5-10 min while long breaks are 15-30 min. The Pi will also recommend activities for the user to do during the break. One suggestion is taken from the user input in the set up about favorite break time activities. The second suggestion is from a curated list of activities saved on the Pi. Here is a sample of this aspect of the the proposed conversation design. 

Short breaks:
![Short Breaks](https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%203/pt2_conversation_design_short-breaks.png)

Long breaks:
![Long Breaks](https://github.com/meyhaa/Interactive-Lab-Hub/blob/Fall2021/Lab%203/pt2_conversation_design_long-breaks.png)

*Include videos or screencaptures of both the system and the controller.*

This video is an overview of the wizard-ing set up system:
[![Video with interaction](https://img.youtube.com/vi/gITt3XY0Mh8/maxresdefault.jpg)](https://youtu.be/gITt3XY0Mh8)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

I recruited Rohan Reddy ([link here](https://youtu.be/fvAqdDV8T9Q)) and Sara Wang ([link here](https://youtu.be/MboVItdB4so)) to interact with my system. 

Answer the following:

### What worked well about the system and what didn't?
The multimodal design of the system worked much better. For example, having users be able to press the button to indicate they are back from break worked better than having it be a fully speech oriented interaction.  

### What worked well about the controller and what didn't?

Staging the intial set up conversation with shell files worked well. But once I had to step in as the voice of the system, it became difficult to control and handle the multi-modal nature of the system. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
My overall main takeaway from WoZ was that it allowed me to think less about the technical feasibility of the systems responses and focus more on the core of the interaction. In part 1 of the lab, especially in the video, I found it really difficult to "be the device" and not let the thoughts of technical feasibility limit my responses. But interacting with the WoZ really got the wheels turning in terms of thinking about the future works here in designing a more autonomous version of the system. 

Here are the main takeaways: 

(1) I was really intrigued by the WoZ accelerometer visualization. Accelerometers have been documented in the literature for stress detection from smartphones and wearables. It would be really interesting to further explore ways to integrate an accelerometer sensor in the system as a way of measuring a user's stress levels.

(2) It would be beneficial to automatically detect using the camera or microphone when the user is back from breaks, especially the 15-30 min longer break time frame. The proximity sensor could also be used instead. 

(3) Separate web page for the initial part of the interaction: users listing out the tasks, estimating length of study session, and discussing their favorite short/long break activities. This would also allow users to not only leverage the speech recognition but also be able to edit or update their responses.

(4) A screen with a timer. It would’ve been really helpful to have a screen with a dynamic timer that provides users with continuous visual feedback about the amount of time left in their session/break. This would allow for the user to be more aware of the time rather than relying on just the speech based output. 

(3) and (4) could also be combined into one UI. 

(5) The ultimate takeaway here is just how many moving parts autonomous systems have. Staging the interaction and pretending to be the device was enough of a challenge. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

My system could be used to create a dataset of interaction for monitoring the study habits/patterns of students, as it relates to their stress levels throughout the course of a semester. It would also be interesting to see how productivity changes depending on how users interact with the device. In terms of different modalities, the acclerometer may be insightful to capture related to stress. Furthermore, the joystick sensor feels very much like a fidget toy and could be used to track restlessness. 
