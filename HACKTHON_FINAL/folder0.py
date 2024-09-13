import tkinter as tk
from tkinter import filedialog

# Function to browse and select folder
def browse_folder():
    folder_selected = filedialog.askdirectory()  # Opens file explorer to select a folder
    if folder_selected:  # If a folder is selected, update the entry widget
        folder_path.set(folder_selected)

# Create the main application window
root = tk.Tk()
root.title("Folder Browser")
root.geometry("500x150")

# Variable to store the folder path
folder_path = tk.StringVar()

# Create and position the text entry box
entry_box = tk.Entry(root, textvariable=folder_path, width=50)
entry_box.grid(row=0, column=1, padx=10, pady=10)

# Create and position the label next to the entry box
label = tk.Label(root, text="Folder Path:")
label.grid(row=0, column=0, padx=10, pady=10)

# Create and position the browse button
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
