import tkinter
import ttkbootstrap as ttk
import os
from ttkbootstrap.constants import *
from tkinter import filedialog as fd
from windowstates import WindowStates
from datamodel import DataModel


class EncryptionView:
    def __init__(self, window):
        self._selected_file_path = str()
        self._selected_key_path = str()
        self._selected_action = None
        
        self._window = window
        self._frame = ttk.LabelFrame(self._window, text="Encryption", padding=10)
        self._encrypt_btn = None
        self._file_name_text = tkinter.StringVar()
        self._key_name_text = tkinter.StringVar()
        self._ready_for_encryption = False
        self.__setup_view()


    def __setup_view(self):
        self._window.rowconfigure(0, weight=1)

        self._frame.pack(fill='x', padx=20, pady=15)

        file_select_frame = ttk.Frame(self._frame)
        file_select_frame.pack()

        ttk.Label(file_select_frame, text="Encrypted file") \
           .grid(row=0, column=0)

        ttk.Button(file_select_frame, text='Select', command=self.__select_file) \
           .grid(row=0, column=1)

        ttk.Label(file_select_frame, textvariable=self._file_name_text) \
           .grid(row=1, column=0)
        
        ttk.Label(file_select_frame, text="Public key") \
           .grid(row=2, column=0)

        ttk.Button(file_select_frame, text='Select', command=self.__select_key) \
           .grid(row=2, column=1)

        ttk.Label(file_select_frame, textvariable=self._key_name_text) \
           .grid(row=3, column=0)

        for widget in file_select_frame.winfo_children():
            widget.grid_configure(padx=10, pady=(0, 10))

        self._encrypt_btn = ttk.Button(self._frame, text='Encrypt',
                                       command=self.__encrypt)
        self._encrypt_btn.pack(expand=True, fill='x', pady=(0, 10))
        self.__disable_btn()

        go_back_btn = ttk.Button(self._frame, text="Return to menu",
                                 command=self.__main_menu, style='Info.TButton')
        go_back_btn.pack(expand=True, fill='x')


    def __enable_btn(self):
        self._encrypt_btn.config(state=NORMAL)

        
    def __disable_btn(self):
        self._encrypt_btn.config(state=DISABLED)


    def __try_enable(self):
        if self._selected_file_path and self._selected_key_path:
            self.__enable_btn()


    def __select_file(self):
        selected = fd.askopenfilename(
            title='Select the file to encrypt',
            filetypes=(('all files', '*'),)
        )

        if not selected:
            return

        _, filename = os.path.split(selected)
        self._file_name_text.set(filename)
        self._selected_file_path = selected
        self.__try_enable()


    def __select_key(self):
        selected = fd.askopenfilename(
            title='Select the public key',
            filetypes=(('pem files', '*.pem'),)
        )

        if not selected:
            return

        _, filename = os.path.split(selected)
        self._key_name_text.set(filename)
        self._selected_key_path = selected
        self.__try_enable()


    def __main_menu(self):
        self._selected_action = WindowStates.MAIN_MENU
        self.__close()


    def __encrypt(self):
        self._selected_action = WindowStates.ENCRYPTION
        self.__close()
        
        
    def __close(self):
        self._frame.destroy()
        self._window.quit()
        
        
    def run(self, data):
        self._window.mainloop()


    def collect(self):
        data = DataModel(self._selected_file_path, self._selected_key_path)
        return (data, self._selected_action)
