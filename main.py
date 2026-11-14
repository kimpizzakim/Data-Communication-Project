
import tkinter as tk
from tkinter import messagebox

def text_to_binary():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Enter some text!")
        return

    binary = ' '.join(format(byte, '08b')
                      for byte in text.encode('utf-8'))

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, binary)

def binary_to_text():
    binary = input_box.get("1.0", tk.END).strip()

    try:
        bits = binary.split()

        if not bits or any(
            len(byte) != 8 or set(byte) - {'0', '1'}
            for byte in bits
        ):
            raise ValueError

        text = bytes(
            int(byte, 2) for byte in bits
        ).decode('utf-8')

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, text)

    except (ValueError, UnicodeDecodeError):
        messagebox.showerror(
            "Error",
            "Enter valid 8-bit binary groups!"
        )


def clear():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Binary Text Converter")
root.geometry("600x450")
root.configure(bg="#eaf2f8")

title = tk.Label(
    root,
    text="Binary Text Converter",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8"
)
title.pack(pady=20)

tk.Label(root, text="Enter Text or Binary:",
         bg="#eaf2f8").pack()

input_box = tk.Text(root, height=5, width=60)
input_box.pack(pady=10)

tk.Button(root, text="Text to Binary",
          command=text_to_binary).pack(pady=5)

tk.Button(root, text="Binary to Text",
          command=binary_to_text).pack(pady=5)

tk.Button(root, text="Clear",
          command=clear).pack(pady=5)

tk.Label(root, text="Output:",
         bg="#eaf2f8").pack(pady=5)

output_box = tk.Text(root, height=5, width=60)
output_box.pack(pady=10)

root.mainloop()
