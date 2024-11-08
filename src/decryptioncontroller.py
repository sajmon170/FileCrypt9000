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
            messagebox.showinfo(message="File decrypted successfully.")
        except FileNotFoundError:
            messagebox.showerror(message="Selected file does not exist.")
        except ValueError:
            messagebox.showerror(message="This key does not match the data.")
        except TypeError:
            messagebox.showerror(message="This is not a private key.")

    def collect(self):
        return (DataModel(), WindowStates.MAIN_MENU)
