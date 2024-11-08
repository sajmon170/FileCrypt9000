from enum import Enum
from enum import auto


class WindowStates(Enum):
    QUIT = auto()
    MAIN_MENU = auto()
    ENCRYPTION_MENU = auto()
    DECRYPTION_MENU = auto()
    ENCRYPTION = auto()
    DECRYPTION = auto()
    KEYGEN = auto()
