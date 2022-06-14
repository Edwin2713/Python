
def caracter (texto,letra):     
    cont1=0   
    for i in range(len(texto)):    
        if letra == texto[i]:
            cont1=cont1+1                 
    return cont1,len(texto)

def run():

    caracter(["ab","a"], "a")

if __name__ == '__main__':
    run()