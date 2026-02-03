import json
from todo_relacionado_con_fecha import fechinguiri 
from factura_PERFECTA import factura 
class eventoun:
    def __init__(self):
        self.evento = self.cargar_eventos()  # cargamos los eventos anteriores
        self.entregado ="entregado.json"
        #self.dias_disponibles = self.sugerir_siguiente_fecha()
    def guardar_entregado(self , factura , transportista):
            try:
                with open("entregado.json", "r") as f:
                    bitacora = json.load(f)
            except FileNotFoundError:
                bitacora = []
            registro = {"transportista": transportista , "factura": factura , "estado": "ENTREGADO"}
            bitacora.append(registro)
            with open("entregado.json", "w") as f:
                json.dump(bitacora, f, indent=4)
    # Guardar en archivo
    def guardar_eventos(self):
        with open("eventos.json", "w") as f: # w modificar archivo
            json.dump(self.evento, f, indent=4)

    # Cargar desde archivo
    def cargar_eventos(self):
        try:
            with open("eventos.json", "r") as f: # r leer archivo
                return json.load(f)
        except FileNotFoundError:
            return []

    def agregar_factura(self):
        print("Selecciona el dia de la entrega\n")
        dias_disponibles = self.sugerir_siguiente_fecha()
        self.mostrar_fechas(dias_disponibles)
        if not dias_disponibles:
            print("No hay fechas disponibles entre esos dias ")
            return None
        try:
            sel = int(input("Seleccione el dia haciendo uso del numero que le antecede\n"))
            if 1<= sel<=len(dias_disponibles):
                dias_de_venta = dias_disponibles[sel-1]
            else:
                print("Seleccion invalida")
                return None
        except ValueError:
            print("Por favor ingrese un numero valido")
            return None
        f = factura().go()
        if f is None:
            print("Introduciste datos incorrectos anteriormente no se pudo crear la factura")
            return None
        banana = {'fecha': dias_de_venta, 'factura': f }
        self.evento.append(banana)
        self.guardar_eventos()  # guardamos cada vez que agregamos
        print("~~~~~~~FACTURA AÑADIDA CORRECTAMENTE~~~~~~~")

    def eliminar(self):
        while True:
            print("Estos son sus textos\n")
            self.leer_facturas()
            eliminar = input(f"Numero de la factura que desea eliminar (ESC : para volver):\n")
            if eliminar.upper() == "ESC":
                 break
            if not eliminar.isdigit():
                print("Introduce un numero valido")
                continue
            indice = int(eliminar)-1
            if 0 <= indice < len(self.evento):
                c = input(f"Este es su texto {self.evento[indice]['factura']}\n\n (SI o NO):\n")
                if c.upper() == "SI":
                    confirmacion = input(f"Seguro que desea eliminarlo:(SI o NO):\n")
                    if confirmacion.upper() == "SI":
                        self.evento.pop(indice)
                        self.guardar_eventos()  # guardamos después de eliminar
                        print("ELIMINANDO ...")
                        break
                    else:
                        print("RETORNAMOS")
            break

    def leer_facturas(self):
        print("\n --- TUS FACTURAS GUARDADAS --- ")
        for i, e in enumerate(self.evento, start=1):
            print(f"{i}. Fecha: {e['fecha']} - Factura: {e['factura']}\n")

    def repeticion(self):
        contador = {}
        for fechas in self.evento:
            fecha = fechas['fecha']
            if fecha not in contador :
                contador[fecha] = 1
            elif contador[fecha] < 3:
                contador[fecha] +=1
            else:
                return "debe cambiar de dia"
        return contador
    
    def filtrado(self , fecha):
        resultados = []
        for factura in self.evento:
            if factura['fecha'] == fecha:
                resultados.append(factura)
        return resultados
    
    def sugerir_siguiente_fecha(self):
        conteos = self.repeticion()
        dias_disponibles = []
        print("Entre que dias desea el envio")
        primer_dia = fechinguiri().date()
        segundo_dia = fechinguiri().date()
        print(f"Buscando fechas disponibles entre {primer_dia} y {segundo_dia}")
        while primer_dia <= segundo_dia:
            if primer_dia not in conteos:
                dias_disponibles.append(primer_dia)
                primer_dia = (primer_dia[0]+1, primer_dia[1], primer_dia[2])
        return dias_disponibles
    
    def mostrar_fechas(self,a):
        print("Estas son las fechas disponibles para la entrega:\n")
        for i , n in enumerate(a, start = 1):
            print (f"{i} . {n}\n")

#manana hacer commit
#cambiar todo el proyecto a data time para manejar fechas con mas facilidad
#verificacion de stock disponible antes de agregar factura
#xq el transportista no retorna