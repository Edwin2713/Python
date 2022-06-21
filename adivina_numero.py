import random

def run():

    numero_random = random.randint(1,100)
    numero_user = int(input('ingrese un numero del 1 al 100:  '))

    while numero_user != numero_random:
        if numero_user < numero_random:
            print('MAS GRANDE')            
        else:
            print('MAS PEQUEÑO')
        numero_user = int(input('ingrese otro numero:  '))

    print('     !!!!!!    GANASTE      !!!!!!    ')
    
    
    
    
if __name__ == '__main__':
    run()