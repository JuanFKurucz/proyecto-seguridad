from src.crud.user import create_user, connect_user


def ask(text):
    return input(f"{text}: \n")


def menu(logged_user=None):
    if logged_user is not None:
        print("=== Menu (Logged) ===")
        opcion = ask("1 - Encriptar archivo\n2 - Desencriptar archivo\n3 - Desconectarse")
        if opcion == "1" or opcion == "2":
            file_in = ask("Ingrese ruta del archivo actual")
            file_out = ask("Ingrese ruta del archivo nueva")
            if opcion == "1":
                logged_user.encrypt_file(file_in, file_out)
            else:
                logged_user.decrypt_file(file_in, file_out)
        elif opcion == "3":
            return menu(None)
    else:
        print("=== Menu (Not logged) ===")
        opcion = ask("1 - Conectarse\n2 - Registrarse\n3 - Salir")
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
        elif opcion == "3":
            quit()
    return menu(logged_user)


if __name__ == "__main__":
    print("Bienvenido al software")
    menu()
