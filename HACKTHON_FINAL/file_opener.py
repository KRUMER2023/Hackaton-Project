import tkinter as tk
import os
import doc

def open_file(parent):
    global root
    
    # Destroy the previous popup window
    parent.destroy()
    root = None  # Reset the push_popup variable
    file=doc.fname()
    os.startfile(file)