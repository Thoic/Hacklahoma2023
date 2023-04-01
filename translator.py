import cv2
import pytesseract
import os
from gtts import gTTS

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cam_port = 0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()

if result:
	cv2.imwrite("scannedImage.jpg", image)
else:
	print("Image detection error")

image = cv2.imread('scannedImage.jpg')
translation = pytesseract.image_to_string(image)
print(translation)
gttsObj = gTTS(text=translation, lang='en', slow=False)
gttsObj.save("translation.mp3")
  
os.system("start translation.mp3")