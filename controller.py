# run to use cv mouse
####### Needed matterial and Ideas ##########
# 1. will need to take photos with given interval 
# and save each 2nd to last as previous so when i first see a click i can use the both eye
# images for that click location
#
# 2. mouse needs to run in a loop
#   - need photo taker
#   - need eye state checker - will use math at first and possibly transition to ml
#   - if state has one closed then use ai model to determine location
#   -  need a function that clicks on a given location input
#   - if mouse clicks (we missed) then save that for next training cycle. retrain after every 100?
#
# 3. for training the AI model gather 1000 clicks and images then train before starting the loop 
#   - maybe still do straining screen for extremes (corners and halfway points)

######### Imports #########
from pynput.mouse import Button, Controller
import cv2
###########################
def on_click(x, y, button, pressed):
    if pressed:
        # grab photo then save

def start():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    mouse = Controller()
    cap = cv2.VideoCapture(0)
    running = True # change to something more controlling
    previous_states = (1,1)
    previous_img = None
    while running:
        ### check states in loop
        if state[0] == 0 and previous_states[0] == 1:
            location = EyeMouse_model(images)
            mouse.press(Button.right)
            mouse.release(Button.right)
        else:
            previous_img = cap.read()


        # if missed location and mouse had to click then record for training


if __name__=="__main__":
    start()