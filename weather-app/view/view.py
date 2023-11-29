import tkinter
from tkinter.constants import *
from tkinter.ttk import *


class View(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
    
    def main(self):
        self.mainloop()