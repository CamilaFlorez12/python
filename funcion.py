from lista import primos
def num_primos():
    num_primo=input("Ingrese un numero")
    primo=num1%2==0
    if primo==False:
        primo=primos.append(num_primo)
    else:
        print("No es un numero primo")
    
        


def pares_primos():
    num1=int(input("Ingrese un numero"))
    num=num1+2
    if num1 in primos:
        limite=num1+2
        for num1 in range(num1,limite,2):
            num=num1+2
            print(num)
    return num
    
    
def palindromicos_primos():
    num1=input("Ingrese un numero")
    if num1 in primos:
        for num1 in range[10]:
            palindromo= num1 in [-1]==num1 in [1]
            print(palindromo)
    return 
