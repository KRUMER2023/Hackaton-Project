import tkinter as tk
import pyautogui

def show_pressed_popup(parent):
    global root
    
    # Destroy the previous popup window
    parent.destroy()
    root = None  # Reset the push_popup variable
    
    # Get the current cursor position again
    x, y = pyautogui.position()

    # Create a new root window for the "Pressed" message
    pressed_popup = tk.Tk()
    pressed_popup.overrideredirect(True)
    pressed_popup.attributes('-topmost', True)

    # Set the window position
    pressed_popup.geometry(f"+{x + 10}+{y}")

    # Create a label with the text "Pressed"
    label = tk.Label(pressed_popup, text="Pressed", font=("Arial", 14), bg="black", fg="white", padx=10, pady=5)
    label.pack()

    # Set the duration for how long the pop-up will stay (e.g., 3 seconds)
    pressed_popup.after(3000, pressed_popup.destroy)
    
    pressed_popup.mainloop()

def create_push(parent):
# Create a button with the text "Push"
    button_push = tk.Button(parent, text="Push", bg="black", fg="white", font=("Arial", 7), padx=10, pady=5, command=lambda: show_pressed_popup(parent))
    button_push.pack(side=tk.LEFT)