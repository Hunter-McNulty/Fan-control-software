import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fan control")
        self.geometry("500x500")
        Fanframe(self,2)
        Fanframe(self,4)


class Fanframe(tk.Frame):
    def __init__(self, parent, fannum):
        tk.Frame.__init__(self, parent)
        self.grid(column=0, row=fannum)
        self.speed1 = tk.DoubleVar()
        self.scale = tk.Scale(self, variable=self.speed1, from_= 1, to = 100, orient="horizontal")
        self.scale.grid(column=0, row=0)

if __name__ == "__main__":
    window = Window()
    window.mainloop()