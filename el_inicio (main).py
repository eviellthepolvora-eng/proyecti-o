from todo_relacionado_con_fecha import fechinguiri
from impor import eventoun
from transporte import transportista
from almacen_clases import almacen
class correr_todo:
    print("Buen dia señor")
    print("Que dia es hoy")
    hoy = str(fechinguiri().date())
    # meter el dia
    c = transportista()
    a = eventoun()
    f = almacen()
    while True:
        print("\nComo puedo servirle ?\n")
        print("1 . Vizualizar trabajos pendientes")
        print("2 . Tomar nuevos pedidos")
        print("3 . Verificar disponibilidad")
        print("4 . Salir\n")
        #try:
        OPCION = int(input("ELIJA UNA OPCION\n"))
        if OPCION == 1:
            a.leer_facturas()
            b = a.repeticion()
            d = a.filtrado(hoy)
            for e in b:
                if e == hoy:
                    print(f"Hoy toca hacer la entrega de {b[e]} pedidos")
                    print("Estos son los pedidos a entregar\n")
                    for i , n in enumerate(d, start = 1):
                        print(f"{i}. {n['factura']}\n")
                    print("Asignando transportistas...\n")
            c.usar_carro(d)
            print("Entregas realizadas con exito\n")
            f.eliminacion_modelo()
        elif OPCION == 2:
            a.agregar_factura()
        elif OPCION == 3:
            while True:
                print("\n1 . Ver inventario")
                print("2 . Añadir motos al inventario")
                print("3 . Ver modelos con stock bajo")
                print("4 . Volver al menu principal\n")
                try:
                    opcion_almacen = int(input("Elija una opcion\n"))
                    if opcion_almacen == 1:
                        f.mostrar_vertical(f.al)
                    elif opcion_almacen == 3:
                        f.sin_stock()
                    elif opcion_almacen == 2:
                        f.almacenado()
                    elif opcion_almacen == 4:
                        break
                except ValueError:
                    print("Por favor ingrese un numero valido\n")
        elif OPCION == 4:
            print("Saliendo del programa...")
            break
        #except ValueError:
        #    print("Por favor ingrese un numero valido\n")