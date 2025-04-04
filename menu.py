from funcion import*
menu= """
    Bienvenido al meu:
    1.Encontrar y mostrar pares de numeros primos gemelos
    2.Encontrar y mostrar pares de numeros palindromicos
    3.Salir
    """
menu_pares_primos="""
Bienvenido al menu de pares primos
1.Mostrar pares de numeros primos gemelos
2.Salir
"""
menu_pares_palindromos="""
Bienvenido al menu de primos palindromos
1.Ver primos palindromos
2.Salir
"""

def mostrar_opc():
    return input("Ingrese la opcion deseada")
def menu_principal():
    print(menu)
def menu_pares():
    while True:
        print(menu_pares_primos)
        opc=mostrar_opc()
        if opc=="1":
            limite= int(input("Ingrese un numero limite:"))
            primos_gemelos=pares_primos(limite)
            print(f"paraes primos gemelos hasta {limite}: {primos_gemelos}")
            pares_primos(limite)
        elif opc=="2":
            input("Enter Pass......")
            break
        else:
            print("Ingrese una opcion valida")
                
def menu_palindromos():
    while True:
        print(menu_pares_palindromos)
        opc=mostrar_opc()
        if opc=="1":
            palindromicos_primos()
                            
        elif opc=="2":
            input("Enter Pass........")
            break
        else:
            print("Ingrese una opcion valida")

def funcion():    
    while True:
        menu_principal()
        opc=mostrar_opc()
        if opc=="1":
            menu_pares()
        elif opc=="2":
            menu_palindromos()
        elif opc=="3":
            input("Enter Pass.....")
            print("Saliendo...")
            break
        else:
            print("Ingrese una opcion valida")
funcion()