from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend 

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    return kdf.derive(password.encode())

def encrypt_file(filename, password):
    salt = b'salt_123'
    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB8(salt), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(filename, 'rb') as file:
        plaintext = file.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open('encrypted_' + filename, 'wb') as file:
        file.write(ciphertext)

    print(f'File {filename} encrypted and saved as encrypted_{filename}')

def main():
    filename = input("Enter the name of the file to encrypt: ")
    password = input("Enter the encryption password: ")

    encrypt_file(filename, password)

if __name__ == "__main__":
    main()
