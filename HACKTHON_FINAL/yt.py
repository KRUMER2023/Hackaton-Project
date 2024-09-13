import tkinter as tk
import pyautogui,pyperclip,time,webbrowser
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets3\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def exitW(parent2):
    parent2.destroy()

def Open_yt(parent,query):
    parent.destroy()
    query.replace(' ','+')
    # URL of the website you want to open
    
    webbrowser.open(query)

def YT_Menu(parent):
    
    parent.destroy()
    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    text = pyperclip.paste()
    yt_link='https://www.youtube.com/results?search_query='
    
    
    Open_yt(yt_link+text+'&sp=CAA%253D')
   
def YT_Menu2(parent):
    parent.destroy()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    text = pyperclip.paste()
    yt_link='https://www.youtube.com/results?search_query='
    
    window = Tk()

    window.geometry("325x241")
    window.configure(bg = "#070707")


    canvas = Canvas(
        window,
        bg = "#070707",
        height = 241,
        width = 325,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        162.0,
        120.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Open_yt(window,yt_link+text+'&sp=CAA%253D'),
        relief="flat"
    )
    button_1.place(
        x=27.0,
        y=24.0,
        width=264.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Open_yt(window,yt_link+text+'&sp=CAI%253D'),
        relief="flat"
    )
    button_2.place(
        x=27.0,
        y=73.0,
        width=264.0,
        height=40.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Open_yt(window,yt_link+text+'&sp=CAM%253D'),
        relief="flat"
    )
    button_3.place(
        x=27.0,
        y=122.0,
        width=264.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Open_yt(window,yt_link+text+'&sp=CAE%253D'),
        relief="flat"
    )
    button_4.place(
        x=27.0,
        y=171.0,
        width=264.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()

# YT_Menu2()