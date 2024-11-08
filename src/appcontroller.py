from mainmenuview import MainMenuView
from encryptionview import EncryptionView
from decryptionview import DecryptionView
from encryptioncontroller import EncryptionController
from decryptioncontroller import DecryptionController
from keygencontroller import KeygenController
from windowstates import WindowStates
from programwindow import ProgramWindow

class AppController:
    def __init__(self):
        self._views = {
            WindowStates.MAIN_MENU: MainMenuView,
            WindowStates.ENCRYPTION_MENU: EncryptionView,
            WindowStates.DECRYPTION_MENU: DecryptionView,
            WindowStates.ENCRYPTION: EncryptionController,
            WindowStates.DECRYPTION: DecryptionController,
            WindowStates.KEYGEN: KeygenController
        }

        self._program = ProgramWindow()
        self._current_state = WindowStates.MAIN_MENU
        self._current_view = None
        self._data = None


    def __update(self):
        ViewClass = self._views[self._current_state]
        self._current_view = ViewClass(self._program.window)
        self._current_view.run(self._data)
        self._data, next_state = self._current_view.collect()
        self._current_state = next_state
        

    def run(self):
        while self._current_state != WindowStates.QUIT \
              and self._current_state is not None:
            self.__update()
