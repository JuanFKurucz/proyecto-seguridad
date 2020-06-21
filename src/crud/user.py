import os
from datetime import datetime, timedelta

from src.database.models.user import User  # noqa
from src.database.models.file import File  # noqa
from src.database.session import db_session  # noqa
from src.utils.hash import hash_pass
from sqlalchemy.orm.exc import NoResultFound

from src.utils.cipher import encrypt_file, decrypt_file

from src.utils.hash import hash_md5, generate_token
from src.utils.mail_sender import send_mail_login


def create_user(username, email, password):
    user = User(username=username, email=email, hashed_password=hash_pass(username, password))
    try:
        db_session.add(user)
        db_session.commit()
        db_session.flush()
        return user
    except:
        db_session.rollback()
        return None


def connect_user(username, password):
    user = db_session.query(User).filter(User.username == username).first()
    if user and user.check_password(password=password):
        user.login_token = str(generate_token())
        user.login_token_expiration = (datetime.now() + timedelta(minutes=5)).timestamp()
        db_session.add(user)
        db_session.commit()
        db_session.flush()
        send_mail_login(str(user.email), user.login_token)
        return user
    return None


def encrypt_user_file(user, path, key):
    if not key:
        print("Error: se debe ingresar una clave")
        return
    if not path:
        print("Error: se debe ingresar una ruta de archivo")
        return

    nonce, ciphertext, mac = encrypt_file(hash_md5(key).encode("utf8"), path)
    if not ciphertext:
        print("Error al encriptar el archivo, puede que el archivo que quiera encriptar este vacio")
        return
    user.files.append(
        File(name=os.path.basename(path), encrypted_file=ciphertext, nonce=nonce, mac=mac)
    )
    db_session.commit()


def decrypt_user_file(user, file_id, path, key):
    if not path:
        print("No se especifico una ruta de archivo para guadar")
        return
    try:
        decrypt_file(
            hash_md5(key).encode("utf8"),
            db_session.query(File).filter(File.id == file_id).one(),
            path,
        )
    except NoResultFound:
        print("El archivo no existe")
    except Exception:
        print("Error inesperado")


def check_token_user(user, token):
    if user.login_token and user.login_token_expiration:
        date = datetime.fromtimestamp(user.login_token_expiration)
        if (date - datetime.now()).total_seconds() > 0:
            if user.login_token == token:
                return True
            else:
                print("Token invaldo")
        else:
            print("Token expirado")
    return False
