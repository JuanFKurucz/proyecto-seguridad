from src.database.models.user import User  # noqa
from src.database.session import db_session  # noqa
from src.utils.security import hash_pass


def login(username, password):
    user = db_session.query(User).filter(User.usuario == username).first()
    if user and user.check_password(password=password):
        return user
    return None


def sign_up(username, email, password):
    user = User(usuario=username, email=email, hashed_password=hash_pass(password))
    try:
        db_session.add(user)
        db_session.commit()
        db_session.flush()
        return user
    except:
        db_session.rollback()
        return None


def ask(text):
    return input(f"{text}: \n")


def menu(logged_user=None):
    if logged_user is not None:
        print("=== Menu (Logged) ===")
        opcion = ask(" - ")
    else:
        print("=== Menu (Not logged) ===")
        opcion = ask("1 - Conectarse\n2 - Registrarse")
        if opcion == "1":
            username = ask("Ingrese su usuario")
            password = ask("Ingrese su contraseña")
            user = login(username, password)
            if user:
                return menu(user)
            else:
                print("Intento de conexion fallida")
        elif opcion == "2":
            username = ask("Ingrese su usuario")
            email = ask("Ingrese su email")
            password = None
            while True:
                password = ask("Ingrese su contraseña")
                if ask("Ingrese su contraseña denuevo") == password:
                    break
            user = sign_up(username, email, password)
            if user:
                return menu(user)
            else:
                print("Intento de registro fallido")
    return menu(logged_user)


def run():
    print("Bienvenido al software")
    menu()


if __name__ == "__main__":
    run()
