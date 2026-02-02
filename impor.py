import json
from todo_relacionado_con_fecha import fechinguiri 
class eventoun:
    def __init__(self):
        self.evento = self.cargar_eventos()  # cargamos los eventos anteriores
        self.entregado ="entregado.json"
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
        dias_de_venta = fechinguiri().date()
        from factura_PERFECTA import factura 
        if not dias_de_venta:
            print("Haga otra eleccion\n")
            return None
        if dias_de_venta[-1] == []:
            print("FECHA INCORRECTA")
            return None
        else:
            nueva_fecha = dias_de_venta
            f = factura().go()
            if f == "Factura inválida":
                return None
            else:
                banana = {'fecha': str(nueva_fecha), 'factura': f }
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

   # def run(self):
   #     while True:
   #         print("\n OPCIONES :")
   #         print("1. AGREGAR FACTURA")
   #         #print("2. LEER FACTURAS")
   #         print("3. ELIMINAR FACTURA")
   #         print("4. SALIR")
   #         OPCION = input("ELIGE UNA OPCION:\n ")
   #         if OPCION == "1":
   #             self.agregar_factura()
   #         elif OPCION == "2":
   #             self.leer_facturas()
   #         elif OPCION == "3":
   #             self.eliminar()
   #         elif OPCION == "4":
   #             print("Saliendo ... ")
   #             break
   #         else:
   #             print("Opcion inválida intente denuevo")
