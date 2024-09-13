
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import Tray_menu
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Tray_menu import run_tray_icon
from NoteItUp_main import popup_main
import threading


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Win3(parent):
    
    window = Tk()
    parent.destroy()
    window.geometry("440x86")
    window.configure(bg = "#070707")


    canvas = Canvas(
        window,
        bg = "#070707",
        height = 86,
        width = 440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        11.0,
        19.0,
        429.0,
        67.0,
        fill="#010000",
        outline="")

    canvas.create_text(
        91.0,
        35.0,
        anchor="nw",
        text="Application is running in background",
        fill="#FFFFFF",
        font=("Inter", 15 * -1)
    )
    window.resizable(False, False)
    # Set the duration for how long the pop-up will stay (e.g., 3 seconds)
    window.after(3000, window.destroy)
    
    tray_thread = threading.Thread(target=run_tray_icon)
    
    # Start the tray icon in the background
    tray_thread.start()

    # Run the popup_main function in the main thread
    popup_main()
    
    # window.mainloop()