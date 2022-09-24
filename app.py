# Importing important libraries
from tkinter import image_names
import cv2
from PIL import Image
import speech_recognition as sr
import pytesseract as tr
from playsound import playsound
import time


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

translate_dict = { ' ':'/', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

message = input("Enter your message: ")
message = " ".join(translate_dict[c] for c in message.upper())


def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound("dot.mp3")
            #time.sleep(0.3)
        elif c == "-":
            playsound("dash.mp3")
            #time.sleep(0.3)    
        elif c =="/" or c == " ":
            time.sleep(0.5)    
        else:
            print("Invalid")    

print(message)
play_morse_code(message) 
