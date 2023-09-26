# Eye state detection model

########## IMPORTS #################
from screeninfo import get_monitors
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from pynput.mouse import Listener
import threading

########## Global Variables ########
CLICK_COUNT = 0
MAX_CLICKS = 2

####################################

def get_screen_resolution():
    # Get a list of all monitors connected to the system
    monitors = get_monitors()
    return monitors[0].width, monitors[0].height

def on_click(x, y, button, pressed):
    global CLICK_COUNT
    if pressed:
        CLICK_COUNT += 1
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def generate_screen(width, height):
    def on_start():
        label.pack(fill=tk.BOTH, expand=tk.YES)
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()
    
    def on_closing():
        img.close()
        root.destroy()
    img = Image.new("RGB", (width, height), "white")

    # Draw a single red dot in the center (you can adjust the dot's position)
    draw = ImageDraw.Draw(img)
    dot_radius = 5
    dot_position = (width // 2, height // 2)
    draw.ellipse(
        [
            dot_position[0] - dot_radius,
            dot_position[1] - dot_radius,
            dot_position[0] + dot_radius,
            dot_position[1] + dot_radius,
        ],
        fill="red",
    )
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    window_thread = threading.Thread(target=on_start)
    window_thread.daemon = True
    window_thread.start()
    listener = Listener(on_click=on_click)
    listener.start()
    previous = 0
    while CLICK_COUNT < MAX_CLICKS:
        if CLICK_COUNT > previous:
            draw.ellipse(
                [
                    dot_position[0] - dot_radius,
                    dot_position[1] - dot_radius,
                    dot_position[0] + dot_radius,
                    dot_position[1] + dot_radius,
                ],
                fill="while",
            )
            dot_position = ()
            draw.ellipse(
                [
                    dot_position[0] - dot_radius,
                    dot_position[1] - dot_radius,
                    dot_position[0] + dot_radius,
                    dot_position[1] + dot_radius,
                ],
                fill="red",
            )


            photo = ImageTk.PhotoImage(img)
            label.config(image=photo)
            label.image = photo
            root.update_idletasks()
            root.update()
    on_closing() 
    listener.stop()


if __name__ == "__main__":
    # Get the screen resolution
    # width, height = get_screen_resolution()
    # print(width, height)
    width, height = 600, 600 # test
    # create screen
    generate_screen(width, height)