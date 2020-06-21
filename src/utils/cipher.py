from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from src.utils.config import CIPHER_KEY


def encrypt_file(current_path, output_path):
    with open(current_path, "rb") as file_in:
        data = file_in.read()
        cipher = AES.new(CIPHER_KEY, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))
        with open(output_path, "wb") as file_out:
            file_out.write(cipher.iv)
            file_out.write(ciphered_data)
            file_out.close()


def decrypt_file(current_path, output_path):
    with open(current_path, "rb") as file_in:
        iv = file_in.read(16)
        ciphered_data = file_in.read()
        file_in.close()

        cipher = AES.new(CIPHER_KEY, AES.MODE_CBC, iv=iv)
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        with open(output_path, "wb") as file_out:
            file_out.write(original_data)
            file_out.close()


