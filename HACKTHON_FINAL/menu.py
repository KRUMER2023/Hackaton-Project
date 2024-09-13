import tkinter as tk

AI_root = None

def exitW(parent2):
    parent2.destroy()

def AI_Menu(parent):
    global AI_root
    AI_root = tk.Tk()
    parent.destroy()
    
    # Get the screen width and height
    screen_width = AI_root.winfo_screenwidth()
    screen_height = AI_root.winfo_screenheight()
    
    # Calculate the x-coordinate for the window to appear at the center of the left side of the screen
    x_coord = 0
    
    # Calculate the y-coordinate for the window to appear at the center of the screen
    y_coord = (screen_height - 200) // 2
    
    # Set the window size and position
    AI_root.geometry("400x300+{}+{}" .format(x_coord, y_coord))  
    AI_root.resizable(False, False)  # Make the window non-resizable

    # Remove window decorations (title bar, etc.) and keep the window on top
    AI_root.overrideredirect(True)
    AI_root.attributes('-topmost', True)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(AI_root, bg="grey")
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

    # Create the buttons
    button_you = tk.Button(button_frame, text="Exit", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5,command=lambda:exitW(AI_root))
    button_you.pack(fill=tk.X, pady=5)
    
    button_you = tk.Button(button_frame, text="AI", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_you.pack(fill=tk.X, pady=5)

    button_me = tk.Button(button_frame, text="TRANSLATION", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_me.pack(fill=tk.X, pady=5)

    button_all = tk.Button(button_frame, text="VIDEO TO TEXT", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_all.pack(fill=tk.X, pady=5)

    button_nothing = tk.Button(button_frame, text="DICTIONARY", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_nothing.pack(fill=tk.X, pady=5)

    # Start the GUI event loop
    AI_root.mainloop()
# AI_Menu()