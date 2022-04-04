import cv2
from cvzone.PoseModule import PoseDetector
from tkinter import *
main_window = Tk()
#main_window.geometry('750x400')
Label(main_window, text="GenOS BioTracker").grid(row=1, column=2)
Label(main_window, text="Live camera test:").grid(row=3, column=2)
hello = StringVar()
def on_click1():
    detector = PoseDetector()
    cap = cv2.VideoCapture(0) #the value 0 signifies to make sure it reads from the camera
    while True:
        success, img = cap.read()
        img =detector.findPose(img)
        cv2.imshow("Result", img)
        c = cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
Button(main_window, text="Start wireframing camera", command=on_click1).grid(row=3, column=4)
Label(main_window, text="Prerecorded video test(Enter the name of the video along with file extension):").grid(row=10, column=2)
video_name = Entry(main_window, textvariable=hello ,width=25, borderwidth=5).grid(row=10, column=3)
print(str(video_name))
def on_click2():
    video_name1 = hello.get()
    detector = PoseDetector()
    cap = cv2.VideoCapture(video_name1)
    while True:
        success, img = cap.read()
        img =detector.findPose(img)
        #video.write(img)
        cv2.imshow("Result", img)
        c = cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
Button(main_window, text=" Show wireframe output  " , command=on_click2).grid(row=10, column=4)
main_window.mainloop()