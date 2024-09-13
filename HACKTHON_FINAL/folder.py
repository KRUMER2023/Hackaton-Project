import tkinter as tk
import os
import doc

def open_folder(parent):
    global root
    
    # Destroy the previous popup window
    parent.destroy()
    root = None  # Reset the push_popup variable
    folder=doc.fold()
    os.startfile(folder)
    

def create_OF(parent):
# Create a button with the text "Push"
    button_push = tk.Button(parent, text="D", bg="black", fg="white", font=("Arial", 7), padx=10, pady=5, command=lambda: open_folder(parent))
    button_push.pack(side=tk.LEFT)
