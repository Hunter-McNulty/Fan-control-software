import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fan control")
        self.geometry("500x500")


if __name__ == "__main__":
    window = Window()
    window.mainloop()