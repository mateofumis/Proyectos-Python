import os
import sys
# Obtener Path actual
pwd = os.getcwd()

def mkdir():
    # Crear directorio en la Ruta actual con nombre elegido por el Usuario
    new_folder = input("[+] Ingrese el nombre de la carpeta: ")
    new_folder_path = os.path.join(pwd, new_folder)
    # Valdiar que no exista la carpeta indicada por el Usuario
    if os.path.exists(new_folder):
        print("\n[-] Ya existe un directorio con ese nombre en la ruta actual")
        what_now()
    else:
        os.mkdir(new_folder_path)
        print("\n[+] Se creó el directorio con éxito en la siguiente ruta: ", new_folder_path)
        what_now()

def rmdir():
    # Obtener el nombre de la carpeta que el Usuario desea eliminar
    folder_to_delete = input("[+] Ingrese el nombre de la carpeta que desea borrar: ")
    folder_to_delete_path = os.path.join(pwd, folder_to_delete)
    # Valdiar que la carpeta a borrar existe
    if os.path.exists(folder_to_delete):
        os.rmdir(folder_to_delete_path)
        print("\n[+]Se borró con éxito el siguiente directorio: ", folder_to_delete_path)
        what_now()
    else:
        print("\n[-] La carpeta no existe, por favor intente con otro nombre")
    what_now()

# Definir función para decidir qué hacer luego
def what_now():
    wanna = input("\n[+] ¿Desea volver al menú? (yes/y) - (no/n): ")
    if wanna == "yes":
        menu()
    elif wanna == "y":
        menu()
    elif wanna == "no":
        sys.exit()
    elif wanna == "n":
        sys.exit()
    else:
        print("[-] Opción incorrecta")
        what_now()


# Mostrar menú de opciones
def menu():
    options = '''1) Crear carpta
2) Borrar carpeta
3) Salir del script'''
    print(options)
    choice = input("Seleccione una opción: ")
    if choice == "1":
        mkdir()
    elif choice == "2":
        rmdir()
    elif choice == "3":
        print("[+] Saliendo del script...")
        sys.exit()
    else:
        print("[-] Opción incorrecta")
        menu() 

# Funcion principal
def main():
    print("="*20)
    print("$$ Folder Manager $$")
    print("="*20)
    menu()

# Thanks for review my script
if __name__ == "__main__":
    main()
