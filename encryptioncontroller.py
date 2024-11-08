from windowstates import WindowStates
from datamodel import DataModel
from cryptotools import encrypt
from tkinter import messagebox


class EncryptionController:
    def __init__(self, window):
        self._window = window
    
    def run(self, data):
        try:
            encrypt(data.filename, data.key)
            messagebox.showinfo(message="Plik zaszyfrowano pomyślnie.")
        except FileNotFoundError:
            messagebox.showerror(message="Wybrany plik nie istnieje.")
        except ValueError:
            messagebox.showerror(message="Ten klucz nie pasuje do danych.")
        except TypeError:
            messagebox.showerror(message="To nie jest klucz publiczny.")
        

    def collect(self):
        return (DataModel(), WindowStates.MAIN_MENU)
