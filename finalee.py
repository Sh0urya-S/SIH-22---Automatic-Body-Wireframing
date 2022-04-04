from enum import Flag
import cv2
# from cvzone.PoseModule import PoseDetector
from tkinter import *
main_window = Tk()
#main_window.geometry('750x400')
Label(main_window, text="GenOS BioTracker").grid(row=1, column=2)
Label(main_window, text="Live camera test:").grid(row=3, column=2)
hello = StringVar()

import mediapipe as mp
# flag=0

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
# flag= 2

def on_click1():

    click(0)
def on_click2():
    click(1)


def click(flag):
    video_name1 = hello.get()
    # detector = PoseDetector()
    if flag==0:
        cap = cv2.VideoCapture(0)    
    elif flag==1:
        cap = cv2.VideoCapture(video_name1)
    while cap.isOpened():
        # read frame from capture object
        _, frame = cap.read()

        try:
            # convert the frame to RGB format
            RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # process the RGB frame to get the result
            results = pose.process(RGB)

            print(results.pose_landmarks)
            # draw detected skeleton on the frame
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # show the final output
            cv2.imshow('Output', frame)
        except:
            break
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()





Button(main_window, text="Start wireframing camera", command=on_click1).grid(row=3, column=4)
Label(main_window, text="Prerecorded video test(Enter the name of the video along with file extension):").grid(row=10, column=2)
video_name = Entry(main_window, textvariable=hello ,width=25, borderwidth=5).grid(row=10, column=3)



Button(main_window, text=" Show wireframe output  " , command=on_click2).grid(row=10, column=4)

main_window.mainloop()