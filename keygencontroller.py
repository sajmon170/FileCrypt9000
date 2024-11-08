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
            messagebox.showinfo(message="Klucze zostały wygenerowane pomyślnie.")
        except FileExistsError:
            messagebox.showerror(message="W tym katalogu istnieje już klucz.")
        

    def collect(self):
        return (DataModel(), WindowStates.MAIN_MENU)
