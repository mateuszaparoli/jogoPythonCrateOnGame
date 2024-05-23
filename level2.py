import tkinter as tk
from tkinter import messagebox

# Function to execute player code
def run_code():
    player_code = code_editor.get("1.0", tk.END)
    try:
        exec(player_code)
        messagebox.showinfo("Success", "Code executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Python Quest - Level 2")
root.geometry("800x600")

# Instructions
instructions = tk.Label(root, text="Welcome to Python Quest - Level 2!\nTask: Draw shapes and display text using Tkinter.\n\nWrite the following code:\n1. Create a Canvas widget.\n2. Draw a rectangle on the canvas.\n3. Display a text message on the canvas.", justify="left")
instructions.pack(pady=10)

# Code editor
code_editor = tk.Text(root, height=20, width=80, font=("Consolas", 12))
code_editor.pack(pady=20)

# Run button
run_button = tk.Button(root, text="Run Code", command=run_code)
run_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
