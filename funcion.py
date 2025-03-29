def num_primos(n):
    if n < 2:
        return False
    for i in range(2,n):
            if n % i == 0:
                return False
    return True
    
def pares_primos(limite):
    primos_gemelos=[]
    for num in range(2,limite -1):
        if num_primos(num) and num_primos(num+2):
            primos_gemelos.append((num, num +2))
    return primos_gemelos
    
def es_palindromo(n):
    return str(n) == str(n)[::-1]

def palindromicos_primos(limite):
    primos_palin=[]
    for num in range(10,limite):
        if num_primos(num) and es_palindromo(num):
            primos_palin.append(num)
    return primos_palin
