#factura viene saliendo de la factura q se guarda en el json
class transportista:
    def __init__(self):
        self.trans = ["Pancho" , "Juan","Ernesto"]
        self.facturas_pendientes = None     
    def existe_factura(self,factura):
        if len(factura) > 0:
           return True
        if not factura:
           return False
    def carro_disponible(self):
        if not self.trans:
            print("No hay transporte disponible")
            return None
        else:
            for i , n in enumerate(self.trans ,start = 1):
                print(f"Transportadores {i} - {n}")
            select = int(input(f"Escoja el transportador\n"))
            if not select :
                return None
            if select <= len(self.trans):
                return self.trans[select-1]
            else : return None
    def usar_carro(self , factura):
        while True == self.existe_factura(factura):
            dispo = self.carro_disponible()
            self.trans.remove(dispo)
            return f"El encargado de entregar la factura {factura} es {dispo}"
#factura ={"hola":1}
#a = transportista() 
#print(a.usar_carro(factura))
# la idea es q al momento de usar el carro se quite de la lista de transportistas disponibles
# y asi no se pueda volver a usar hasta q se termine la entrega
# luego de terminar la entrega se vuelve a agregar a la lista de transportistas disponibles {como gestiono esto}
# asi se puede llevar un control de los transportistas disponibles
#segunda tarea
#agendarle turno al en correspondencia con la factura q le toca entregar

