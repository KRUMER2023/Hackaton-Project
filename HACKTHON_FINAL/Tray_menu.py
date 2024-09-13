import pystray
import PIL.Image
from gui import popup_main
import threading
import os
from tkinter import filedialog,messagebox

image = PIL.Image.open("exe_icon.ico")

def on_tray_clicked(icon, item):
    if str(item) == "Say Hello":
        print("hello world")
    elif str(item) == "Update":
        messagebox.showerror("Upadate Status", "Coming soon..........")
    elif str(item) == "Exit":
        os._exit(0)

# Function to start the tray icon in a separate thread
def run_tray_icon():
    icon = pystray.Icon("Temp", image, menu=pystray.Menu(
        pystray.MenuItem("Continue", on_tray_clicked),
        pystray.MenuItem("Pause", on_tray_clicked),
        pystray.MenuItem("Update", on_tray_clicked),
        pystray.MenuItem("Exit", on_tray_clicked)
    ))
    icon.run()

# def start():
#     tray_thread = threading.Thread(target=run_tray_icon)
    
#     # Start the tray icon in the background
#     tray_thread.start()

#     # Run the popup_main function in the main thread
#     popup_main(folder,docx_name)

#     # Optionally join the tray thread if you want the main thread to wait for it
#     tray_thread.join()
