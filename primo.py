def es_primo(numero):
      
    cont=0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i ==0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False

def run():

    num = int(input('Escribe un numero:'))
    
    if es_primo(num):
        print('Es Primo')
    else:
        print('No es Primo')


if __name__ == "__main__":
    run()