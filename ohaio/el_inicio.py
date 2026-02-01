from todo_relacionado_con_fecha import fechinguiri
from impor import eventoun
class correr_todo:
    print("Buen dia señor")
    print("Que dia es hoy")
    hoy = str(fechinguiri().date())
    # meter el dia
    while True:
        print("Como puedo servirle ?\n")
        print("1 . Vizualizar trabajos pendientes")
        print("2 . Tomar nuevos pedidos")
        print("3 . Verificar disponibilidad")
        OPCION = int(input("ELIJA UNA OPCION\n"))
        if OPCION == 1:
            a = eventoun().leer_facturas()
            b = eventoun().repeticion()
            for c in b :
                if c == hoy:
                    print(f"Hoy toca hacer la entrega de {b[c]} pedidos")
            # solo queda mostrar los pedidos
            # SI ALGUNA COINCIDE ENTONCESS HAY UN TRANSPORTISTA MENOS Y UNA MOTO MENOS
            print("YES") 
        elif OPCION == 2:
            # QUE EL CLIENTE SELECCIONE UNA FECHA Y TOMAR LA FACTURA
            print("YES") 
        elif OPCION == 3:
            # EN CASO DE QUE SE ACABE LA MERCANCIA HACER UN TEXTO DE "SIN STOCK"
            # EN CASO DE QUE QUEDEN 5 MOTOS O MENOS HACER UN TEXTP "POCO STOCK"
            print("YES") 