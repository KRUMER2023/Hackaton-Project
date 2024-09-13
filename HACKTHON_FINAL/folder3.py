import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to browse and select folder
def browse_folder():
    folder_selected = filedialog.askdirectory()  # Open file explorer to select a folder
    if folder_selected:  # If a folder is selected, update the entry widget
        folder_path.set(folder_selected)

# Function to browse and select a DOCX file in the chosen folder
def browse_docx_file():
    folder = folder_path.get()  # Get the folder path from the first text box
    if not os.path.isdir(folder):  # Check if the folder path is valid
        messagebox.showerror("Invalid Folder", "Please select a valid folder first.")
        return

    docx_file = filedialog.askopenfilename(initialdir=folder, filetypes=[("Word Documents", "*.docx")])
    if docx_file:  # If a file is selected, update the docx file entry box
        docx_file_name.set(os.path.basename(docx_file))  # Get only the file name without the path

# Function to validate the folder and DOCX file and show result or error
def validate_selection():
    folder = folder_path.get()
    docx_file = docx_file_name.get()

    # Check if the folder is valid
    if not os.path.isdir(folder):
        messagebox.showerror("Invalid Folder", "Please select a valid folder.")
        return
    
    # Check if the DOCX file exists in the selected folder
    docx_file_path = os.path.join(folder, docx_file)
    if not docx_file.lower().endswith('.docx') or not os.path.isfile(docx_file_path):
        messagebox.showerror("Invalid File", f"'{docx_file}' does not exist in the selected folder.")
        return

    # Show success message if both folder and file are valid
    messagebox.showinfo("Success", f"Folder: {folder}\nDOCX File: {docx_file_path} is valid.")

# Create the main application window
root = tk.Tk()
root.title("Folder and DOCX File Selection")
root.geometry("550x200")

# Variable to store the folder path and DOCX file name
folder_path = tk.StringVar()
docx_file_name = tk.StringVar()

# Folder selection widgets
label_folder = tk.Label(root, text="Folder Path:")
label_folder.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_folder = tk.Entry(root, textvariable=folder_path, width=40)
entry_folder.grid(row=0, column=1, padx=10, pady=10)

button_browse_folder = tk.Button(root, text="Browse", command=browse_folder)
button_browse_folder.grid(row=0, column=2, padx=10, pady=10)

# DOCX file name selection widgets
label_docx_file = tk.Label(root, text="DOCX File Name:")
label_docx_file.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_docx_file = tk.Entry(root, textvariable=docx_file_name, width=40)
entry_docx_file.grid(row=1, column=1, padx=10, pady=10)

button_browse_docx = tk.Button(root, text="Browse", command=browse_docx_file)
button_browse_docx.grid(row=1, column=2, padx=10, pady=10)

# Create the "Next" button
next_button = tk.Button(root, text="Next", command=validate_selection)
next_button.grid(row=2, column=1, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
