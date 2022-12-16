import random

def passwordGenerator(num):
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    simbolos = ["#","$","!","&","-","_","*"]
    numeros = ["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0"]

    caracteres = mayusculas +  minusculas + simbolos + numeros
    contrasena = []

    for num in range(num):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        
    contrasena = "".join(contrasena)
    return contrasena

def main():
    print("="*25)
    print("GENERADOR DE CONTRASEÑAS")
    print("="*25)
    num = input("Longitud de la contraseña: ")
    num = int(num)
    contrasena = passwordGenerator(num)
    print(f"Contraseña aleatoria y segura generada correctamente: {contrasena}")

if __name__ == "__main__":
    main()
