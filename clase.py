import Pyro4

class Empresa:
    #inicializacion del objeto
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.acciones=100
        self.valor=10000
    #Definicion de metodos
    def comprarA(self,num):
        self.acciones=self.acciones-num
        self.valor=self.valor+(10*num)
    def venderA(self,num):
        self.acciones=self.acciones+num
        self.valor=self.valor-(10*num)
@Pyro4.expose
class Bolsa:
    #Vectores para almacenar informacion de las empresas
    empresas=[]
    historial=[]
    def agregarE(self,nombre):
        codigo=len(self.empresas)+1
        self.empresas.append(Empresa(nombre,codigo)) #se agrega valores al vector empresas
        txt='La empresa '+nombre+' se agrego a la bolsa'
        print(txt)
        return txt
    def listar(self):
        txt='Empresa||'+'Codigo||'+'Acciones||'+'Valor'+'\n'
        #Imprimir lista de empresas ingresadas 
        for i in self.empresas:
            txt=txt+str(i.nombre)+'\t'+str(i.codigo)+'\t'+str(i.acciones)+'\t'+str(i.valor)+'\n'
        print(txt)
        return txt
        
    def comprarB(self,num,codigo):
        for i in self.empresas:
            #Se compara el codigo de la empresa
            if(i.codigo==codigo):
            #Si se existe ese codigo se realiza la compra de acciones
                i.comprarA(num)
                txt='Se compro '+str(num)+' acciones en '+i.nombre
                print(txt)
                return txt
    def venderB(self,num,codigo):
        for i in self.empresas:
            #Comparacion de empresas ingresadas por su codigo 
            if(i.codigo==codigo):
                #Si existe esa empresa se procede a la venta de acciones
                i.venderA(num)
                txt='Se vendieron '+str(num)+' acciones en '+i.nombre
                print(txt)
                return txt




