from windowstates import WindowStates
from datamodel import DataModel
from cryptotools import generate_keys
from tkinter import messagebox


class KeygenController:
    def __init__(self, window):
        self._window = window
    
    def run(self, data):
        try:
            generate_keys(data.filename)
            messagebox.showinfo(message="Keys generated successfully.")
        except FileExistsError:
            messagebox.showerror(message="This directory already contains a key.")
        

    def collect(self):
        return (DataModel(), WindowStates.MAIN_MENU)
