#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import subprocess
from time import sleep

subprocess.call(['sh','./shell_scripts/start_first_session.sh'])

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('desk_keras_model.h5')

# Load Labels:
labels=[]
f = open("desk_labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    full_label = ' '.join(line.split(' ')[1:]).strip()
    print(full_label)
    labels.append(full_label)
    
subprocess.call(['sh','./shell_scripts/first_session_complete.sh'])
sleep(2)
subprocess.call(['sh','./shell_scripts/start_break.sh'])
previous_prediction = ''
break_time = True
away = False
while(break_time):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    if labels[np.argmax(prediction)] != previous_prediction:
        previous_prediction = labels[np.argmax(prediction)]
        print("Predicted Location:",labels[np.argmax(prediction)])
    if labels[np.argmax(prediction)] == 'Not at Desk':
        away = True
    if away and labels[np.argmax(prediction)] == 'Desk':
        subprocess.call(['sh','./shell_scripts/end_break.sh'])
        sleep(2)
        subprocess.call(['sh','./shell_scripts/resume_tasks_HW_helper.sh'])
        break_time = False

    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
