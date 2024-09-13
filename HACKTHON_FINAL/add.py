import tkinter as tk
import pyautogui
from docx import Document
from docx.shared import Pt
import time  # Import the time module
import pyperclip
import saveNames
from doc import file_maker,fname
import stack

button_add=tk
dragging = False


def append_text_to_doc(text):
    
    name= fname()
    doc = Document(name)
    doc.add_paragraph(text)
    doc.save(name)
    stack.set_action(text)
    print(f"Appended text: {text}")
    

def add_text_to_doc(parent):
    parent.destroy()
    # Copy the selected text to the clipboard (assumes the user has selected text)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    selected_text = pyperclip.paste()
    
    if selected_text:
        append_text_to_doc(selected_text)

# def create_add(parent):
#     # Create a button with the text "Push"
#     button_push = tk.Button(parent, text="T+", bg="black", fg="white", font=("Arial", 7), padx=10, pady=5, command=lambda: add_text_to_doc(parent))
#     button_push.pack(side=tk.LEFT)