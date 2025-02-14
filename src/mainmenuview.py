import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog as fd
from windowstates import WindowStates
from datamodel import DataModel


class MainMenuView:
    def __init__(self, window):
        self._selected_action = None
        self._selected_directory = None
        
        self._window = window 
        self._frame = ttk.LabelFrame(self._window, text="Mode select", padding=10)
        self.__setup_view()

        
    def __setup_view(self):
        self._frame.pack(fill='x', padx=20, pady=15, ipadx=50)

        
        ttk.Button(self._frame, text='Encrypt', command=self.__encrypt) \
            .pack(expand=True, fill='x', pady=(0, 10))

        ttk.Button(self._frame, text='Decrypt', command=self.__decrypt) \
            .pack(expand=True, fill='x', pady=(0, 10))

        ttk.Button(self._frame, text='Generate keys', command=self.__keygen) \
            .pack(expand=True, fill='x')


    def __encrypt(self):
        self._selected_action = WindowStates.ENCRYPTION_MENU
        self.__close()


    def __decrypt(self):
        self._selected_action = WindowStates.DECRYPTION_MENU
        self.__close()

        
    def __keygen(self):
        selected = fd.askdirectory(
            title='Select the save directory'
        )

        if not selected:
            return

        self._selected_directory = selected
        self._selected_action = WindowStates.KEYGEN
        self.__close()


    def __close(self):
        self._frame.destroy()
        self._window.quit()
        

    def run(self, data):
        self._window.mainloop()


    def collect(self):
        return (DataModel(self._selected_directory, None),
                self._selected_action)
