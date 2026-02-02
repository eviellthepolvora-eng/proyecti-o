#factura viene saliendo de la factura q se guarda en el json
from impor import eventoun
class transportista:
    def __init__(self):
        self.trans = ["Pancho" , "Juan","Ernesto"]
        self.facturas_pendientes = None     
    def existe_factura(self, factura):
        if factura is None:
           #ver el hasattr como funciona 
            return False
        if len(factura) > 0:
            return True
        return False
    def carro_disponible(self):
        if not self.trans:
            print("No hay transporte disponible")
            return None
        else:
            for i , n in enumerate(self.trans ,start = 1):
                print(f"Transportadores {i} - {n}")
            self.select = int(input(f"Escoja el transportador\n"))
            if not self.select :
                return None
            if self.select <= len(self.trans):
                return self.trans[self.select-1]
            else : return None
    def usar_carro(self , factura):
        if not self.existe_factura(factura):
            print("No hay facturas disponibles")
            return None
        dispo = self.carro_disponible()
        if dispo is None:
            print("No hay transportistas disponibles")
            return None
        self.trans.remove(dispo)
        primer = factura[0]
        print(f"El encargado de entregar la factura {primer['factura']} es {dispo}\n")
        ev = eventoun()
        ev.guardar_entregado(primer['factura'] , dispo)
        # Eliminar la factura de eventos.json (persistir)
        ev.evento.remove(primer)
        factura.pop(0)
        ev.guardar_eventos()
        # Recursión solo si hay más facturas
        if len(factura) > 0:
            return self.usar_carro(factura)
#factura ={"hola":1}
#a = transportista() 
#print(a.usar_carro(factura))
# la idea es q al momento de usar el carro se quite de la lista de transportistas disponibles
# y asi no se pueda volver a usar hasta q se termine la entrega
# luego de terminar la entrega se vuelve a agregar a la lista de transportistas disponibles {como gestiono esto}
# asi se puede llevar un control de los transportistas disponibles
#segunda tarea
#agendarle turno al en correspondencia con la factura q le toca entregar

