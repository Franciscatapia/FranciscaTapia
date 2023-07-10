'''venta de entradas al concierto VIP de “Michael Jam” que se realizará de forma exclusiva solo para 100 asistentes
'''
from os import system
system("cls")
from datetime import datetime

fechaActual = datetime.now()

Platinum = ["","","","","","","","","",""]
Gold = ["","","","","","","","","",""]
Silver = ["","","","","","","","","",""]

comprador = []

def menu():
    print("""
    \tCreativos.cl\n 
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def Entradas_disponibles():
    system("cls")
    print("***********************ESCENARIO**************************")
    print(" |Fila |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| :")
    print(" |Fila |11| |12| |13| |14| |15| |16| |17| |18| |19| |20| :")
    print(" |Fila |21| |22| |23| |24| |25| |26| |27| |28| |29| |30| :")
    print(" |Fila |31| |32| |33| |34| |35| |36| |37| |38| |39| |40| :")
    print(" |Fila |41| |42| |43| |44| |45| |46| |47| |48| |49| |50| :")
    print(" |Fila |51| |52| |53| |54| |55| |56| |57| |58| |59| |60| :")
    print(" |Fila |61| |62| |63| |64| |65| |66| |67| |68| |69| |70| :")
    print(" |Fila |71| |72| |73| |74| |75| |76| |77| |78| |79| |80| :")
    print(" |Fila |81| |82| |83| |84| |85| |86| |87| |88| |89| |90| :")
    print(" |Fila |91| |92| |93| |94| |95| |96| |97| |98| |99| |100| :")

          
    for fila in range (1,100):
        print(" |  {Platinum, 120.000. (Asientos del 1 al 20)}   | {Gold, 80.000. (Asientos del 21 al 50)}  | {Silver, 50.000. (Asientos del 51 al 100.)} ")
        print("\nEntradas Disponibles")
    input("Presione enter para continuar\n")

def Comprar_Entradas():
    ent_disponibles()
    rut = int(input(" Ingresar rut :"))
    datos_P = [rut]
    Comprador.append(datos_p)
    Cat_entrada = input("\nNombre de cliente :")
    cantidad = cantidad.upper()
    num_entradas =int(input("\nIngresa cantidad de entradas : "))
    if num_entradas ==1:
        num_entradas= 0
    if entrada =="platinum":        
        entrada_p[num_entradas+2] = "X"
    elif entrada =="gold":
        Entrada_G[num_entradas+2] = "X"
    elif entrada =="Silver":
        Entrada_S[num_entrada+2] = "X"
def Lista_Compradores():
    system("cls")
    comprador.sort()
    print("|lista| Run \t| ")
    for compradores in comprador:
        print(f" {compradores+1}  {comprador[compradores]}")
    print("\nLista de compradores")
    input("Enter para finalizar")


def Ganancias_Totales():
    system("cls")
    P = 120000
    G = 80000
    S = 50000
    cantidad =int(input("Ingresa la cantidad de entradas\nque se vendederan por categoria\n==> "))
    total = (p*cantidad)+(g*cantidad)+(s*cantidad)
    print(f"""
    Categoria de entradas |Cantidad |Total
    ______________________________________________________
    categoria P 120000        |{cantidad}        | {a*cantidad}  
    categoria G 80000        |{cantidad}        | {b*cantidad} 
    categoria S 50000       |{cantidad}        | {c*cantidad} 
    ______________________________________________________
           Total         |{cantidad*4}        | {total} """)
    input("Enter para Continuar.. ")

def salir():
    system("cls")
    print(f""" Gracias por usar nuestro servicio {nom_apell}
    Programa utilizado en {fechaActual}""")
    input("Enter para finalizar el programa ")

nom_apell = input("Ingresa tu nombre y apellido, para iniciar el programa : ")   
while True:
    try:
        system("cls")       
        menu()
        op=input("\nIngrese opción una opcion mostrada anteriormente : ")
        match op:
            case "1":
                entradas_disponibles()
            case "2":
                entradas_disponibles()
            case "3":
                entradas_disponibles()
            case "4":
                salir()
            
    except ValueError as op:
        print("Solo los datos numericos dados en pantalla")
.
