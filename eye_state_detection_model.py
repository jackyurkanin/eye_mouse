# Eye state detection model

########## IMPORTS #################
from screeninfo import get_monitors
import numpy as np
import cv2
import random
from pynput.mouse import Listener
import threading

########## Global Variables ########
CLICK_COUNT = 0
MAX_CLICKS = 3

####################################

def get_screen_resolution():
    # Get a list of all monitors connected to the system
    monitors = get_monitors()
    return monitors[0].width+57, monitors[0].height

def on_click(x, y, button, pressed):
    global CLICK_COUNT
    if pressed:
        CLICK_COUNT += 1
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def generate_screen(width, height):
    """
    Generates a black canvas to draw on and gather data for training

    input: width, height of screen
    return: NADA yet
    """
    white = (255,255,255)
    img = np.full((height, width, 3), white, dtype=np.uint8)
    red = (0,0,255)
    coord = [0,0]
    listener = Listener(on_click=on_click)
    listener.start()
    previous = 0
    print('Make fullscreen')
    while CLICK_COUNT < MAX_CLICKS: # check if done gathering
        if CLICK_COUNT > previous: # check if click was made and need to draw new dot
            if previous > 0:
                img = draw(img, white, coord, height, width)
            coord[1] = random.randint(0, width-1)
            coord[0] = random.randint(0, height-1)
            img = draw(img, red, coord, height, width)
            previous += 1

        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print('Finished collecting information')
    
def draw(img, pixel, coord, height, width):
    """
    function for drawing dots on the image
    """
    def get_neightbors(x,y):
        neighs = {(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)}
        return neighs
    img[coord[0],coord[1]] = pixel
    neighbors = get_neightbors(coord[0], coord[1])
    more_neighbors  = set()
    for pix in neighbors:
        more_neighbors.update(get_neightbors(pix[0],pix[1]))
    neighbors.update(more_neighbors)
    for pix in neighbors:  
        if pix[0] < height and pix[1] < width:
                if pix[0] > -1 and pix[1] > -1:
                    img[pix[0],pix[1]] = pixel
    return img

def take_photo():
    """
    takes a photo here and returns the photo as an np.array
    """


    return 

if __name__ == "__main__":
    # Get the screen resolution
    width, height = get_screen_resolution()
    # print(width, height)
    # width, height = 600, 600 # test
    # create screen
    generate_screen(width, height)