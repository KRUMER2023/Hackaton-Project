import tkinter as tk
from tkinter import messagebox

# Function to ensure only one checkbox is selected at a time
def on_check1():
    if chk_var1.get():
        chk_var2.set(0)

def on_check2():
    if chk_var2.get():
        chk_var1.set(0)

# Function to display the chosen file information in a new window
def show_selection():
    if chk_var1.get():
        file_name = entry_new_file.get()  # Get the name from the 'Create New' entry
        if not file_name:
            messagebox.showwarning("Input Error", "Please enter a name for the new file.")
            return
        message = f"Selected Option: Create New File\nFile Name: {file_name}"
    elif chk_var2.get():
        file_name = entry_existing_file.get()  # Get the name from the 'Existing File' entry
        if not file_name:
            messagebox.showwarning("Input Error", "Please enter the name of the existing file.")
            return
        message = f"Selected Option: Use Existing File\nFile Name: {file_name}"
    else:
        messagebox.showwarning("Selection Error", "Please select an option.")
        return

    # Create a new window to display the result
    result_window = tk.Toplevel(root)
    result_window.title("Selection Summary")
    result_window.geometry("300x150")

    # Display the message
    label_result = tk.Label(result_window, text=message, padx=10, pady=10)
    label_result.pack()

# Create the main window
root = tk.Tk()
root.title("File Creation and Selection")
root.geometry("500x200")

# Checkbox variables (0 = unchecked, 1 = checked)
chk_var1 = tk.IntVar()
chk_var2 = tk.IntVar()

# Create the first checkbox and associated widgets
chkbox1 = tk.Checkbutton(root, text="", variable=chk_var1, command=on_check1)
chkbox1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_create_new = tk.Label(root, text="Create New:")
label_create_new.grid(row=0, column=1, padx=10, pady=10, sticky="w")

entry_new_file = tk.Entry(root, width=30)
entry_new_file.grid(row=0, column=2, padx=10, pady=10)

# Create the second checkbox and associated widgets
chkbox2 = tk.Checkbutton(root, text="", variable=chk_var2, command=on_check2)
chkbox2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_existing_file = tk.Label(root, text="Existing File Name:")
label_existing_file.grid(row=1, column=1, padx=10, pady=10, sticky="w")

entry_existing_file = tk.Entry(root, width=30)
entry_existing_file.grid(row=1, column=2, padx=10, pady=10)

# Create the "Next" button
next_button = tk.Button(root, text="Next", command=show_selection)
next_button.grid(row=2, column=1, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
