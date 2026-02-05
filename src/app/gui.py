import tkinter as tk
from app.logic import AppLogic

class SearchBar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Application")
        self.root.geometry("400x300")

        self.logic = AppLogic()

        self.label = tk.Label(self.root, text="Enter your Name:")

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.button = tk.Button(
            self.root, 
            text="Submit", 
            command=self.on_submit
        )
        self.button.pack(pady=10)

        self.output_label = tk.Label(self.root, text="")
        self.output_label.pack(pady=10)

    def on_submit(self):
        name = self.entry.get()
        message = self.logic.generate_message(name)
        self.output_label.config(text=message)

    def run(self):
        self.root.mainloop()


