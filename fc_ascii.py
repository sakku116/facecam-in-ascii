import cv2
import pywhatkit
import os

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # save image
    cv2.imwrite("main.jpg", rgb_frame)

    # convert img to txt
    pywhatkit.image_to_ascii_art("./main.jpg", "main_cvt")

    # print text file content
    with open("./main_cvt.txt", "r") as f:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f.read())

    # cv2.imshow('Eye Controlled Mouse', frame)
    # cv2.waitKey(1)
