from menu import menu_principal,mostrar_opc
from funcion import pares_primos,palindromicos_primos
while True:
    menu_principal()
    opc=mostrar_opc()
    if opc=="1":
        pares_primos()
    elif opc=="2":
        palindromicos_primos()
    elif opc=="3":
        print("Saliendo...")
        break
    else:
        print("Ingrese una opcion valida")
    