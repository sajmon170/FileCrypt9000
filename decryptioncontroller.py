from windowstates import WindowStates
from datamodel import DataModel
from cryptotools import decrypt
from tkinter import messagebox


class DecryptionController:
    def __init__(self, window):
        self._window = window

    def run(self, data):
        try:
            decrypt(data.filename, data.key)
            messagebox.showinfo(message="Plik odszyfrowano pomyślnie.")
        except FileNotFoundError:
            messagebox.showerror(message="Wybrany plik nie istnieje.")
        except ValueError:
            messagebox.showerror(message="Ten klucz nie pasuje do danych.")
        except TypeError:
            messagebox.showerror(message="To nie jest klucz prywatny.")

    def collect(self):
        return (DataModel(), WindowStates.MAIN_MENU)
