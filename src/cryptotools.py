import pickle
import os
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from filemodel import File
from filemodel import EncryptedFile


def get_random_sequence(length):
    return binascii.hexlify(os.urandom(length))


def encrypt(file_path, public_key_path):
    if not os.path.exists(file_path) or not os.path.exists(public_key_path):
        raise FileNotFoundError
    
    symmetric_key = get_random_sequence(length=16)

    with open(public_key_path, 'rb') as public_key_file:
        public_key = RSA.importKey(public_key_file.read())
        rsa_cipher1 = PKCS1_OAEP.new(public_key)
        encrypted_symmetric_key1 = rsa_cipher1.encrypt(symmetric_key)

    src_dir = os.path.dirname(__file__)
    master_key_path = os.path.join(src_dir, "master_key.pem")
        
    with open(master_key_path, 'rb') as public_master_key_file:
        public_master_key = RSA.importKey(public_master_key_file.read())
        rsa_cipher2 = PKCS1_OAEP.new(public_master_key)
        encrypted_symmetric_key2 = rsa_cipher2.encrypt(symmetric_key)
        
    with open(file_path, 'rb') as original_file:
        filename = os.path.basename(file_path)
        content = original_file.read()
        to_encrypt = pickle.dumps(File(filename, content))
        
    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX)
    nonce = aes_cipher.nonce
    encrypted_file, tag = aes_cipher.encrypt_and_digest(to_encrypt)

    current_directory, _ = os.path.split(file_path)
    output_file_path = os.path.join(current_directory,
                                    get_random_sequence(8).decode("utf-8") + '.enc')

    with open(output_file_path, 'wb') as output_file:
        pickle.dump(EncryptedFile(encrypted_symmetric_key1,
                                  encrypted_symmetric_key2,
                                  tag,
                                  nonce,
                                  encrypted_file), output_file)


def decrypt(file_path, private_key_path):
    if not os.path.exists(file_path) or not os.path.exists(private_key_path):
        raise FileNotFoundError
    
    with open(file_path, 'rb') as encrypted_file:
        content = pickle.load(encrypted_file)

    with open(private_key_path, 'rb') as private_key_file:
        private_key = RSA.importKey(private_key_file.read())
        
    try:
        rsa_cipher = PKCS1_OAEP.new(private_key)
        symmetric_key = rsa_cipher.decrypt(content.encrypted_symmetric_key)
    except ValueError:
        rsa_cipher = PKCS1_OAEP.new(private_key)
        symmetric_key = rsa_cipher.decrypt(content.master_key)

    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX, nonce=content.nonce)
    original_file_bytes = aes_cipher.decrypt(content.encrypted_file)
    aes_cipher.verify(content.tag)
    original_file = pickle.loads(original_file_bytes)

    current_directory, _ = os.path.split(file_path)
    output_file_path = os.path.join(current_directory, original_file.filename)

    with open(output_file_path, 'wb') as output_file:
        output_file.write(original_file.content)


def generate_keys(target_dir):
    private_key_path = os.path.join(target_dir, "private_key.pem")
    public_key_path = os.path.join(target_dir, "public_key.pem")
    
    if os.path.exists(private_key_path) or os.path.exists(public_key_path):
        raise FileExistsError

    new_key = RSA.generate(4096)
    private_key_file = open(private_key_path, 'wb')
    private_key_file.write(new_key.export_key('PEM'))
    private_key_file.close()

    public_key_file = open(public_key_path, 'wb')
    public_key_file.write(new_key.publickey().export_key('PEM'))
    public_key_file.close()
