from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    return kdf.derive(password.encode())

def decrypt_file(filename, password):
    salt = b'salt_123'
    key = derive_key(password, salt)

    iv = b'initialization_v'

    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with open(filename, 'rb') as file:
        ciphertext = file.read()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open('decrypted_' + filename, 'wb') as file:
        file.write(decrypted_data)

    print(f'File {filename} decrypted and saved as decrypted_{filename}')

def main():
    filename = input("Enter the name of the file to decrypt: ")
    password = input("Enter the decryption password: ")

    decrypt_file(filename, password)

if __name__ == "__main__":
    main()

