import tkinter as tk
import pyautogui,pyperclip,time,webbrowser

AI_root = None

def exitW(parent2):
    parent2.destroy()

def Open_yt(parent,query):
    parent.destroy()
    query.replace(' ','+')
    # URL of the website you want to open
    
    webbrowser.open(query)

def YT_Menu(parent):
    global AI_root
    AI_root = tk.Tk()
    parent.destroy()
    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the clipboard is updated
    text = pyperclip.paste()
    yt_link='https://www.youtube.com/results?search_query='
    
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
    
    button_you = tk.Button(button_frame, text="Revelence", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5,command=lambda:Open_yt(AI_root,yt_link+text+'&sp=CAA%253D'))
    button_you.pack(fill=tk.X, pady=5)
    
    button_you = tk.Button(button_frame, text="Upload Date", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5,command=lambda:Open_yt(AI_root,yt_link+text+'&sp=CAI%253D'))
    button_you.pack(fill=tk.X, pady=5)

    button_me = tk.Button(button_frame, text="Views", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5,command=lambda:Open_yt(AI_root,yt_link+text+'&sp=CAM%253D'))
    button_me.pack(fill=tk.X, pady=5)

    button_all = tk.Button(button_frame, text="Rating", bg="black", fg="white", font=("Arial", 12), padx=10, pady=5,command=lambda:Open_yt(AI_root,yt_link+text+'&sp=CAE%253D'))
    button_all.pack(fill=tk.X, pady=5)

    # Start the GUI event loop
    AI_root.mainloop()
# AI_Menu()