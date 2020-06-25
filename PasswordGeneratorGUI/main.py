import tkinter as tk
import string
from secrets import choice


class PasswordGen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.length = tk.IntVar()

        # Button to generate password 

        self.generate_button = tk.Button(self.frame, command=lambda: self.generate(self.get_length.get()),
                                         text="Generate Password")

        
        self.show_pass = tk.StringVar()

        # Entry box to display output

        self.show_pass_box = tk.Entry(self.frame, textvariable=self.show_pass, width=40)

        # Slider to determine desired length of password

        self.get_length = tk.Scale(self.frame, length=100, orient=tk.HORIZONTAL, to=128, sliderlength=15)
        
        # Inserting objects to grid

        self.get_length.grid(row=4, column=0)
        self.generate_button.grid(row=5, column=0)
        self.show_pass_label.grid(row=3, column=0)
        self.frame.pack()
    
    # Function that outputs a randomised password consisting of upper and lower case letters, numbers and symbols

    def generate(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join([choice(characters) for i in range(length)])
        self.show_pass.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password generator")
    root.iconbitmap("lockicon.ico")
    root.geometry("275x125")
    PasswordGen(root)
    root.mainloop()