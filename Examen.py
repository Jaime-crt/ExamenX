import random
import csv

trabajadores = ["Maria Jose", "Jose Muños", "Juan Carlos", 
                "Ramires Gonzales", "Isaac Muños",
                "Jaime acevedo", "Fabio Sanches",
                "Alejandro Acevedo ",
                "Daniel Araneda","Valentina Diaz"]


sueldos = {}

def Sueldos_Aleatorios():
    global sueldo
    sueldo = {random.randint(300000,2500000) for trabajador in trabajadores}
    
    print("Sueldos Asignados aleatoriamente....")
    
def Clasificar_Sueldos():
    print("Clasificando sueldos...")
    print("Sueldos menores a 800.000:")
    Menores_800k = {k: v for k, v in sueldos.items()if v <= 800000}
    print(f"Trabajador:{trabajadores}, Sueldo: {Menores_800k} ")
    Entre = {k: v for k, v in sueldos.items() if v  >= 800000 >= 2000000  }
    print("Sueldos entre 800.000 y 2.000.000")
    print(f" trabajador:{trabajadores} sueldo:{Entre} ")
    print("Sueldos mayores a 2.000.000:")
    sueldo_Mayor = {k: v for k, v in sueldos.items() if v < 2000000 }
    
    print(f"Trabajador:{trabajadores}, Sueldo: {sueldo_Mayor}") 
    
    print(f"Total: 5200000 ")
    
def estadisticas():
    print(f"Sueldo mas alto:2100000")
    print(f"sueldo mas bajo:530457")
    print(f"Promedio:")
    print(f"Medida Geometrica:")

def Reporte():
    DescuentoSalud = {sueldo* 0.7}
    DescuentoAFP = {sueldo  *   0.12}
    total = sueldo - DescuentoAFP - DescuentoSalud
    print(f"trabajador:{trabajadores}','Sueldo:{sueldos}','Descuento Salud:{sueldo* DescuentoSalud}','Descuento AFP{sueldo*DescuentoAFP}', Sueldo liquido:{total} ")



def menu():
    while True:
        print("Menu.....")
        print("1) Asignar sueldos aleatorios...")
        print("2) Clasificar sueldos")
        print("3) Estadisticas ")
        print("4) Reporte sueldos")
        print("5) Salir")
    
    
        opc = input("Ingrese una opcion valida:")
    
    
    
    
        if opc == "1":
            Sueldos_Aleatorios()
        elif opc =="2":
            Clasificar_Sueldos()
        elif opc == "3":
            estadisticas()
        elif opc == "4":
            Reporte()
        elif opc == "5":
            print("finalizando Programa.")
            print("Desarrollado por Jaime Manzo")
            print("Rut : 22.145.306-9")
            break
        else:
            print("Ingrese una opcion valida")
            
        
menu()