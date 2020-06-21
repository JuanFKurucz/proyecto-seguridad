from src.crud.user import (
    create_user,
    connect_user,
    encrypt_user_file,
    decrypt_user_file,
    check_token_user,
)
from src.utils.policies import validate_email, validate_password
from src.utils.interface import TimeoutOccurred, ask, ask_password, clear_screen


def menu(logged_user=None):
    try:
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
                    key=ask_password("Ingrese una clave de encriptacion"),
                )
            elif opcion == "3":
                decrypt_user_file(
                    user=logged_user,
                    file_id=ask("Ingrese id del archivo"),
                    key=ask_password("Ingrese una clave de encriptacion"),
                    path=ask("Ingrese ruta del archivo"),
                )
            elif opcion == "4":
                return menu(None)
        else:
            print("=== Menu (Not logged) ===")
            opcion = ask("1 - Conectarse\n2 - Registrarse\n3 - Salir")
            if opcion == "1":
                username = ask("Ingrese su usuario")
                password = ask_password("Ingrese su contraseña")
                user = connect_user(username, password)
                if user:
                    if check_token_user(user, ask("Ingrese el token de acceso enviado a su mail")):
                        return menu(user)
                else:
                    print("Intento de conexion fallida")
            elif opcion == "2":
                username = ask("Ingrese su usuario")
                email = None
                while True:
                    email = ask("Ingrese su email")
                    if validate_email(email):
                        break
                    else:
                        print("El email no es valido")
                print(
                    """
    La contraseña debe tener:
    - Un largo de 8 a 32 caracteres
    - 2 letras en mayuscula
    - 1 caracter especial !@#$&*
    - 2 numerales 0-9
    - 3 letras en minuscula
    """
                )
                password = None
                while True:
                    password = ask_password("Ingrese su contraseña")
                    if validate_password(password):
                        if ask_password("Ingrese su contraseña denuevo") == password:
                            break
                    else:
                        print("La contraseña no cumple con las politicas de seguridad")
                user = create_user(username, email, password)
                if user:
                    return menu(user)
                else:
                    print("Intento de registro fallido")
            elif opcion == "3":
                quit()
        return menu(logged_user)
    except TimeoutOccurred:
        print("\nSe ha desconectado del programa por inactividad")
        quit()


if __name__ == "__main__":
    print("Bienvenido al software")
    menu()
