import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("Simple File explorer")
root.geometry("400x200")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All files", "*.*"), ("Text documents", "*.txt")]
    )

    if file_path:
        file_path_label.config(text=f"Selected file: {file_path}")

browse_button = tk.Button(root, text="Browse Files", command=browse_file)
browse_button.pack(pady=20)

file_path_label = tk.Label(root, text="Selected File: None", wraplength=380)
file_path_label.pack(pady=20)

root.mainloop()