import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to browse and select folder
def browse_folder():
    folder_selected = filedialog.askdirectory()  # Opens file explorer to select a folder
    if folder_selected:  # If a folder is selected, update the entry widget
        folder_path.set(folder_selected)

# Function to validate the path and show it in a new window
def show_folder_path():
    path = folder_path.get()
    if os.path.isdir(path):  # Check if the path is a valid directory
        # Create a new window to display the valid folder path
        result_window = tk.Toplevel(root)
        result_window.title("Selected Folder Path")
        result_window.geometry("400x100")
        
        label_result = tk.Label(result_window, text=f"Selected Folder Path:\n{path}", padx=10, pady=10)
        label_result.pack()
    else:
        messagebox.showerror("Invalid Path", "The folder path entered is invalid. Please enter a valid path.")

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

# Create and position the next button
next_button = tk.Button(root, text="Next", command=show_folder_path)
next_button.grid(row=1, column=1, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
