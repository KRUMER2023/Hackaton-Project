from PyDictionary import PyDictionary
import pyautogui,time,pyperclip
from doc import fname
from docx import Document
import stack

def append_text_to_doc(text):
    
    name= fname()
    doc = Document(name)
    doc.add_paragraph(text)
    doc.save(name)
    stack.set_action(text)
    print(f"Appended text: {text}")

def dictionary(parent):
    parent.destroy()
    # Create a dictionary instance
    dictionary = PyDictionary()

    # Copy the selected text to the clipboard (assumes the user has selected text)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    word = pyperclip.paste()
    # # Get the meaning of a word
    # word = "hypothesis"
    meaning = dictionary.meaning(word)
    # Print the meaning
    print(meaning)
    append_text_to_doc(meaning)