from src.crud.user import (
    create_user,
    connect_user,
    encrypt_user_file,
    decrypt_user_file,
    check_token_user,
)
from src.utils.policies import validate_email, validate_password
from src.utils.interface import TimeoutOccurred, ask, ask_password, clear_screen


def prompt_password(text):
    print(
        f"""
    La {text} debe tener:
    - Un largo de 8 a 32 caracteres
    - 2 letras en mayuscula
    - 1 caracter especial !@#$&*
    - 2 numerales 0-9
    - 3 letras en minuscula
    """
    )
    password = None
    while True:
        password = ask_password(f"Ingrese una {text}")
        if validate_password(password):
            if ask_password(f"Ingrese la {text} denuevo") == password:
                break
            else:
                print("Debe ingresar la misma clave")
        else:
            print(f"La {text} no cumple con las politicas de seguridad")
    return password


def menu(logged_user=None):
    try:
        if logged_user is not None:
            print(f"=== Menu (Logged as {logged_user.username}) ===")
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
                    key=prompt_password("clave de encriptacion"),
                )
            elif opcion == "3":
                file_id = ask("Ingrese id del archivo")
                if file_id:
                    decrypt_user_file(
                        user=logged_user,
                        file_id=file_id,
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
                password = prompt_password("contraseña")
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
    except Exception:
        print("Error inesperado")
        menu(logged_user)


if __name__ == "__main__":
    print("Bienvenido al software")
    menu()
