from src.crud.user import create_user, connect_user


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
            user = connect_user(username, password)
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
            user = create_user(username, email, password)
            if user:
                return menu(user)
            else:
                print("Intento de registro fallido")
    return menu(logged_user)


if __name__ == "__main__":
    print("Bienvenido al software")
    menu()
