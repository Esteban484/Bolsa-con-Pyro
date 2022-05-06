import clase
import Pyro4

#Se especifica que se utiliza el metodo bolsa
Bolsa=clase.Bolsa()

#Inicializacion del servidor mediante Pyro
Pyro4.Daemon.serveSimple({
    Bolsa: 'BOLSA',
}, host="localhost", port=7589, ns=False, verbose=True)

