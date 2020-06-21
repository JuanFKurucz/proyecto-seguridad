from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from src.utils.config import CIPHER_KEY


def encrypy_text(key, text):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv, cipher.encrypt(pad(text, AES.block_size))


def decrypt_text(key, text, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(text), AES.block_size)


def encrypt_file(current_path, output_path):
    try:
        with open(current_path, "rb") as file_in:
            ciphered_iv, ciphered_data = encrypy_text(key=CIPHER_KEY, text=file_in.read())
            with open(output_path, "wb") as file_out:
                file_out.write(ciphered_iv)
                file_out.write(ciphered_data)
                file_out.close()
    except FileNotFoundError:
        print("No se encontro la ruta especificada")


def decrypt_file(current_path, output_path):
    try:
        with open(current_path, "rb") as file_in:
            iv = file_in.read(16)
            ciphered_data = file_in.read()
            file_in.close()
            with open(output_path, "wb") as file_out:
                file_out.write(decrypt_text(key=CIPHER_KEY, text=ciphered_data, iv=iv))
                file_out.close()
    except FileNotFoundError:
        print("No se encontro la ruta especificada")

