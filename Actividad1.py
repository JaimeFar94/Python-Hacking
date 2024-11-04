#Actividad 1 Machine Learning

#Integrantes:
#Angie Morales
#Javier Hernandez
#Jaime Farfan
#Johan Castro
#William Andrés Salavarrieta claros

from os import system
system("cls")

can,ref,total=[],[],[] #declarar vertor
T=7  #son el total de los productos.
D = 5 # Son los Días de la semana

def inicializar(): #inicia los vectores con 0
    for i in range(T * D): # se multiplica los valores para tener el tamaño de los vectores
        can.append(0)
        ref.append(0)
        total.append(0)
        print(can)

def captura():
    for i in range(T * D):
        can[i] = int(input("Digite la cantidad de ventas de la referencia " + str(i % T + 1) + " para el día " + str(i // T + 1) + ": ")) 
    return can
def refrerencias():
    for i in range(T * D):
        ref[i]=int(input("Digite valor de ventas de la refernecia de la referencia de papa frita" + str(i % T + 1) + " para el día " + str(i // T + 1) + ": "))
    return ref

def costos(can, ref):
    for i in range(T): 
        total[i]=can[i]*ref[i]
    return total
def mostrar(can,ref,total):
    tgc=0
    tgv=0
   
    print(can)
    print(ref)
    print(total)

    for i in range(T): 
        for j in range(D): 
            indice = i + j * T
            print("Referencia " + str(i + 1) + ", Día " + str(j + 1) + ": Cantidad " + str(can[indice]) + ", Valor " + str(ref[indice]) + ", Total " + str(total[indice]))
            tgc+= can[indice]
            tgv+= total[indice]
    print("Las ventas totales en unidades de papas fritas es de", tgc)
    print("Las ventas totales en dinero de papas firtas es de", tgv)

    venta = max(total)
    min_venta=min(total)
    idx_max = total.index(venta)
    idx_min = total.index(min_venta)
    print("Venta mayor: Referencia " + str(idx_max % T + 1) + ", Día " + str(idx_max // T + 1) + " - Total " + str(venta))
    print("Venta menor: Referencia " + str(idx_min % T + 1) + ", Día " + str(idx_min // T + 1) + " - Total " + str(min_venta))

def titulo():
    print("Empresa Margarita")
    
def salir():
    print("Chao")


def main():
  
    titulo()
    inicializar()
    can=captura()
    ref=refrerencias()
    total=costos(can, ref)
    mostrar(can,ref,total)
    salir()

#Bloque principal
main()



