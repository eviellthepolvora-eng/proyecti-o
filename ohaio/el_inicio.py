HISTORIAL = "entregado.json"
from todo_relacionado_con_fecha import fechinguiri
from impor import eventoun
from transporte import transportista
from almacen_clases import almacen
class correr_todo:
    print("Buen dia señor")
    print("Que dia es hoy")
    hoy = str(fechinguiri().date())
    # meter el dia
    while True:
        print("\nComo puedo servirle ?\n")
        print("1 . Vizualizar trabajos pendientes")
        print("2 . Tomar nuevos pedidos")
        print("3 . Verificar disponibilidad")
        a = eventoun()
        c = transportista()
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
        elif OPCION == 2:
            a.agregar_factura()
        elif OPCION == 3:
            f = almacen()
            f.almacenado()
            #f.verificar_stock()
            # EN CASO DE QUE SE ACABE LA MERCANCIA HACER UN TEXTO DE "SIN STOCK"
            # EN CASO DE QUE QUEDEN 5 MOTOS O MENOS HACER UN TEXTP "POCO STOCK"
            print("YES") 