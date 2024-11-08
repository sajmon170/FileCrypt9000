import tkinter
import ttkbootstrap as ttk


class ProgramWindow:
    def __init__(self): 
        self.window = tkinter.Tk()
        ttk.Style().theme_use('minty')
        self.window.title("FileCipher9000")
        self.window.resizable(False, False)
        self.window.rowconfigure(0, weight=1)
