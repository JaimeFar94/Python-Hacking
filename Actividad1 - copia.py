#declarar vertor

can,ref,total=[],[],[]
T=7

def inicializar():
    for i in range(T):
        can.append(0)
        ref.append(0)
        total.append(0)
        print(can)
def captura():
    for i in range(T):
        can[i]=int(input("Digite la cantidad de ventas de la referencia de papa frita"))
    return can
def refrerencias():
    for i in range(T):
        ref[i]=int(input("Digite valor de ventas de la refernecia de la referencia de papa frita"))
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
        tgc=tgc+can[i]
    for i in range(T):
        tgv=tgv+total[i]
    print("Las ventas totales en unidades de papas fritas es de ", tgc)
    print("Las ventas totales en dinero de papas firtas es de", tgv)


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



