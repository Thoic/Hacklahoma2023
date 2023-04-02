import cv2
import pytesseract
import os
from gtts import gTTS
import RPi.GPIO as GPIO

def translate(channel):
    print('running translate')

    cam_port = 0 
    cam = cv2.VideoCapture(cam_port)
#   cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#   cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    result, image = cam.read()

    if result:
        cv2.imwrite("scannedImage.jpg", image)  
        
        translation = pytesseract.image_to_string(image)
        print(translation)
        
        if not translation:
            translation = "No text detected"
        gttsObj = gTTS(text=translation.lower(), lang='en', slow=False)
        gttsObj.save("translation.mp3")
      
        os.system("mpg321 translation.mp3")
    else:
        print("Image detection error")



print('setting up pins')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=translate)

message = input("waiting for button, press enter to quit\n\n")

GPIO.cleanup()