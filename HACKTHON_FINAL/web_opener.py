import tkinter as tk
import pyautogui,pyperclip,time,webbrowser
from pathlib import Path


def Open_web(query):
    
    query.replace(' ','+')
    # URL of the website you want to open
    
    webbrowser.open(query)
    
    
def search(parent):
    parent.destroy()
    # Copy the selected text to the clipboard (assumes the user has selected text)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    text = pyperclip.paste()
    yt_link='https://www.bing.com/search?pglt=675&q='
    Open_web(yt_link+text)