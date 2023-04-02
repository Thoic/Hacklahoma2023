import cv2
import pytesseract
import os
from gtts import gTTS

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cam_port = 0
cam = cv2.VideoCapture(cam_port)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
result, image = cam.read()

if result:
	cv2.imwrite("scannedImage.jpg", image)
else:
	print("Image detection error")

image = cv2.imread('scannedImage.jpg')

h, w, c = image.shape
boxes = pytesseract.image_to_boxes(image) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', image)
cv2.waitKey(0)

translation = pytesseract.image_to_string(image).lower()
print(translation)
if(translation == ""):
	translation = "No text detected"
gttsObj = gTTS(text=translation, lang='en', slow=False)
gttsObj.save("translation.mp3")
  
os.system("start translation.mp3")
