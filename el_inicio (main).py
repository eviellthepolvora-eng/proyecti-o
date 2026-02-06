from todo_relacionado_con_fecha import fechinguiri
from impor import eventoun
from transporte import transportista
from almacen_clases import almacen

class correr_todo:
    def __init__(self):
        print("Buen dia señor")
        print("Que dia es hoy")
        fecha_hoy = fechinguiri().date()
        self.hoy = fecha_hoy  # Guardar como tupla, no como string
        self.c = transportista()
        self.a = eventoun()
        self.f = almacen()
        self.ejecutar()
    
    def ejecutar(self):
        while True:
            print("\nComo puedo servirle ?\n")
            print("1 . Vizualizar trabajos pendientes")
            print("2 . Tomar nuevos pedidos")
            print("3 . Verificar disponibilidad")
            print("4 . Salir\n")
            try:
                OPCION = int(input("ELIJA UNA OPCION\n"))
            except ValueError:
                print("Por favor ingrese una opcion valida\n")
                continue
            if not OPCION:
                print("Por favor ingrese una opcion valida\n")
                continue
            if OPCION == 1:
                self.a.leer_facturas()
                b = self.a.repeticion()
                d = self.a.filtrado(self.hoy)
                if d:  # Solo procesar si hay facturas para hoy
                    for e in b:
                        if e == self.hoy:
                            print(f"Hoy toca hacer la entrega de {b[e]} pedidos")
                            print("Estos son los pedidos a entregar\n")
                            for i , n in enumerate(d, start = 1):
                                print(f"{i}. {n['factura']}\n")
                            print("Asignando transportistas...\n")
                    self.c.usar_carro(d)
                    print("Entregas realizadas con exito\n")
                    self.f.eliminacion_modelo()
                else:
                    fecha_str = f"{self.hoy[0]}/{self.hoy[1]}/{self.hoy[2]}"
                    print(f"No hay pedidos para entregar hoy ({fecha_str})\n")
            elif OPCION == 2:
                self.a.agregar_factura()
            elif OPCION == 3:
                while True:
                    print("\n1 . Ver inventario")
                    print("2 . Añadir motos al inventario")
                    print("3 . Ver modelos con stock bajo")
                    print("4 . Volver al menu principal\n")
                    try:
                        opcion_almacen = int(input("Elija una opcion\n"))
                        if opcion_almacen == 1:
                            self.f.mostrar_vertical(self.f.al)
                        elif opcion_almacen == 3:
                            bajo_stock = self.f.sin_stock()
                            if bajo_stock:
                                print("Modelos con stock bajo:")
                                for modelo, cant in bajo_stock.items():
                                    print(f"{modelo}: {cant}")
                            else:
                                print("Todos los modelos tienen stock suficiente")
                        elif opcion_almacen == 2:
                            self.f.almacenado()
                        elif opcion_almacen == 4:
                            break
                    except ValueError:
                        print("Por favor ingrese un numero valido\n")
            elif OPCION == 4:
                print("Saliendo del programa...")
                break

if __name__ == "__main__":
    correr_todo()