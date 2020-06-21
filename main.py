import os

from src.crud.user import create_user, connect_user, encrypt_user_file, decrypt_user_file


def clear_screen():
    os.system("cls")


def ask(text):
    return input(f"{text}: \n")


def menu(logged_user=None):
    if logged_user is not None:
        print(f"=== Menu (Logged as {logged_user.usuario}) ===")
        opcion = ask(
            "1 - Listar archivos encriptados\n2 - Encriptar archivo\n3 - Desencriptar archivo\n4 - Desconectarse"
        )
        if opcion == "1":
            for file in logged_user.files:
                print(f"{file.id} - {file.name}")
            return menu(logged_user)
        elif opcion == "2":
            encrypt_user_file(
                user=logged_user,
                path=ask("Ingrese ruta del archivo"),
                key=ask("Ingrese una clave de encriptacion"),
            )
        elif opcion == "3":
            decrypt_user_file(
                user=logged_user,
                file_id=ask("Ingrese id del archivo"),
                key=ask("Ingrese una clave de encriptacion"),
                path=ask("Ingrese ruta del archivo"),
            )
        elif opcion == "4":
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
