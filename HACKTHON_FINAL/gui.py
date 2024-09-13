
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pynput import mouse
import pyautogui
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets2\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

dragging = False #dragging ko check kar ta hai
window =None

def show_popup():
    
    # Get the current cursor position
    x, y = pyautogui.position()    
    global window # Reference the global add_icon variable
    
    # Destroy the previous "Push" popup if it exists
    if window is not None:
        try:
            window.destroy()
        except tk.TclError:
            pass  # Ignore errors if the window is already destroyed
        
        
    window = Tk()

    window.overrideredirect(True)  # Remove window decorations (title bar, etc.)
    window.attributes('-topmost', True)  # Keep the window on top
    
    # Set the window position (right side of the cursor)
    window.geometry(f"+{x + 10}+{y}")

    window.geometry("381x55")
    window.configure(bg = "#070707")


    canvas = Canvas(
        window,
        bg = "#070707",
        height = 55,
        width = 381,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        190.0,
        27.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=323.0,
        y=11.0,
        width=41.0,
        height=36.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=279.0,
        y=10.0,
        width=41.0,
        height=37.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=235.0,
        y=10.0,
        width=41.0,
        height=37.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=192.0,
        y=11.0,
        width=39.0,
        height=34.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=148.0,
        y=11.0,
        width=39.0,
        height=34.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=104.0,
        y=11.0,
        width=39.0,
        height=34.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=60.0,
        y=11.0,
        width=39.0,
        height=34.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=16.0,
        y=11.0,
        width=39.0,
        height=34.0
    )
    window.resizable(False, False)
    window.mainloop()

def on_click(x, y, button, pressed):
    global dragging,root
    if button == mouse.Button.left:
        if pressed:
            dragging = False  # Reset dragging state on mouse press
        else:
            if dragging:  # Only show popup if dragging occurred
                # show_popup(folder,doc_name)
                show_popup()

def on_move(x, y):
    global dragging
    dragging = True  # If the mouse is moved while pressed, set dragging to True

def popup_main():
    # global folder,doc_name
    # folder=folder
    # doc_name=docx_name
    
    # icon=pystray.Icon("Temp",image,menu=pystray.Menu(
    #     pystray.MenuItem("Continue",on_tray_clicked),
    #     pystray.MenuItem("Pause",on_tray_clicked),
    #     pystray.MenuItem("Update",on_tray_clicked),
    #     pystray.MenuItem("Exit",on_tray_clicked)
    # ))

    # Start listening to mouse events
    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
            listener.join()
            
# popup_main()