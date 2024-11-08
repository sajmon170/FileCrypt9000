from dataclasses import dataclass

@dataclass
class File:
    filename: str
    content: object

@dataclass
class EncryptedFile:
    encrypted_symmetric_key: object
    master_key: object
    tag: object
    nonce: object
    encrypted_file: object
