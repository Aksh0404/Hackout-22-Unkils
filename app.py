# Importing important libraries
from tkinter import image_names
import cv2
from PIL import Image
import speech_recognition as sr
import pytesseract as tr


# for input as per users concert
#   Input as a Image

def choose_img():
  img1 = Image.open("#Desired image path")    # enter desired image's Path
  text0 = tr.image_to_string(img1)
  return text0

def capture_img():

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("cimg")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("cimg", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img1 = "opencv_frame_.png"
            cv2.imwrite(img1, frame)
            print("{} written!".format(img1))
            break

    cam.release()
    cv2.destroyAllWindows()
    text1 = tr.image_to_string(img1)
    return text1

#   Input as Speech 

def voice_input():
    rec = sr.Recognizer()
    mic = sr.Microphone()

    print("Speak Your Word!")
    audio = rec.listen(mic)
    text2 = rec.recognize_google(audio)

    return text2


# Creating File for inputted text

extracted_text = capture_img()

file = open('input_text', 'w')
file.write(extracted_text)

# Processing Part
