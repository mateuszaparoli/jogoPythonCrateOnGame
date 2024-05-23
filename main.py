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
root.title("Python Quest - Level 1")
root.geometry("800x600")

# Instructions
instructions = tk.Label(root, text="Welcome to Python Quest!\nTask: Set up the game window using Tkinter.\n\nWrite the following code:\n1. Import Tkinter\n2. Create a main window\n3. Set the window title to 'Python Quest'\n4. Set the window size to 800x600\n5. Run the Tkinter main loop", justify="left")
instructions.pack(pady=10)

# Code editor
code_editor = tk.Text(root, height=20, width=80, font=("Consolas", 12))
code_editor.pack(pady=20)

# Run button
run_button = tk.Button(root, text="Run Code", command=run_code)
run_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
