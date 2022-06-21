import random
import string

def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)   # convertir lista en string
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es 😂: '+ contrasena)
    print (string.punctuation)
    
    
    
    
if __name__ == '__main__':
    run()