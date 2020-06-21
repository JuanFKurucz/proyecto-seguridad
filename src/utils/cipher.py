from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from src.database.models.file import File


def encrypy_text(key, text):
    """ encrypts plaintext using 256-bit AES in GCM mode """
    cipher = AES.new(key=key, mode=AES.MODE_GCM, mac_len=16)
    ciphertext, mac = cipher.encrypt_and_digest(text)
    return cipher.nonce, ciphertext, mac


def decrypt_text(key: bytes, nonce: bytes, ciphertext: bytes, mac: bytes):
    """ decrypts 256-bit AES encrypted ciphertext """
    cipher = AES.new(key=key, nonce=nonce, mode=AES.MODE_GCM, mac_len=16)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, mac)
        return plaintext
    except ValueError:
        print("Error al desencriptar, clave no correcta")
    except Exception:
        print("Error inesperado")
    return None


def encrypt_file(key, path):
    try:
        with open(path, "rb") as file_in:
            return encrypy_text(key=key, text=file_in.read())
    except FileNotFoundError:
        print("No se encontro la ruta especificada")
    except PermissionError:
        print("Error se necesitan permisos de administrador para ejecutar el programa")
    except Exception:
        print("Error inesperado")
    return None, None, None


def decrypt_file(key, file: File, path_out):
    try:
        text = decrypt_text(key=key, ciphertext=file.encrypted_file, nonce=file.nonce, mac=file.mac)
        if text:
            with open(path_out, "wb") as file_out:
                file_out.write(text)
                file_out.close()
    except FileNotFoundError:
        print("No se encontro la ruta especificada")
    except PermissionError:
        print("Error se necesitan permisos de administrador para ejecutar el programa")
    except Exception:
        print("Error inesperado")

