#!/usr/bin/python3
'''
Author: Mateo Fumis | Github: github.com/mateofumis | LinkedIn: linkedin.com/in/mateo-gabriel-fumis
'''
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
        print("\n[+] Se creó la carpeta con éxito en la siguiente ruta: ", new_folder_path)
        what_now()

def rmdir():
    # Obtener el nombre de la carpeta que el Usuario desea eliminar
    folder_to_delete = input("[+] Ingrese el nombre de la carpeta que desea borrar: ")
    folder_to_delete_path = os.path.join(pwd, folder_to_delete)
    # Valdiar que la carpeta a borrar existe
    if os.path.exists(folder_to_delete):
        os.rmdir(folder_to_delete_path)
        print("\n[+] Se borró con éxito la carpeta:", folder_to_delete)
        what_now()
    else:
        print("\n[-] La carpeta no existe, por favor intente con otro nombre")
    what_now()

def list_directory():
    files_in_pwd = os.listdir(path=pwd) # Obtener la lista de archivos en el path actual
    print(f"Los archivos que se encuentran en el directorio actual son:\n{files_in_pwd}")
    menu()

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
    options = '''
1) Crear carpta
2) Borrar carpeta
3) Listar los archivos de la directorio actual
0) Salir del script
'''
    print(options)
    choice = input("Seleccione una opción: ")
    if choice == "1":
        mkdir()
    elif choice == "2":
        rmdir()
    elif choice == "0":
        print("[+] Saliendo del script...")
        sys.exit()
    elif choice == "3":
        list_directory()
    else:
        print("[-] Opción incorrecta")
        menu() 

# Funcion principal
def main():
    print('''
███████╗ ██████╗ ██╗     ██████╗ ███████╗██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██║     ██╔══██╗██╔════╝██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
█████╗  ██║   ██║██║     ██║  ██║█████╗  ██████╔╝    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔══╝  ██║   ██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝███████╗██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                   ''')
    menu()

# Thanks for review my script
if __name__ == "__main__":
    main()
