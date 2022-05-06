import Pyro4
b=Pyro4.Proxy("PYRO:BOLSA@localhost:7589")
#Metodo que solicita un numero entero
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion valida')
     
    return num

salir = False
opcion = 0
while not salir:
   
    print ("1.-AGREGAR EMPRESA")
    print ("2.-COMPRAR ACCIONES")
    print ("3.-VENDER ACCIONES")
    print ("4.-LISTA DE EMPRESAS")
    print ("5.-SALIR")
   
    print ("ELIGE UNA OPCION")
 
    opcion = pedirNumeroEntero()
    #Se utiliza el metodo para poder agregar una empresa
    if opcion == 1:
        nomE=input("Ingrese el nombre de la empresa:")
        print(b.agregarE(nomE))
    #Compra de una empresa solictandoel codigo y el numero de acciones
    elif opcion == 2:
        codE=int(input("Ingrese el codigo de la empresa:"))
        numA=int(input("Ingrese el numero de acciones a comprar:"))
        txt=b.comprarB(numA,codE)
        print(txt)
    elif opcion == 3:
    #Venta de acciones solictando condigo de empresa y numero de acciones
        codE=int(input("Ingrese el codigo de la empresa:"))
        numA=int(input("Ingrese el numero de acciones a vender:"))
        txt=b.venderB(numA,codE)
        print(txt)
    #Lista de empresas ingresadas al mercado
    elif opcion == 4:
        print(b.listar())
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
 
