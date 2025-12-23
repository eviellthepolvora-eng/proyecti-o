class fechinguiri:
    def entero(self,a):
        e = int(input(a))
        return e
    def fecha(self):
            date = []
            date_valid = False
            print("Este es su calendario")
            print("1 - Seleccione la fecha\n2 - Desea volver atras")
            ELECCION = int(input("Elije una opcion\n"))
            if ELECCION == 1 :
                dia = self.entero("Dia:")
                mes = self.entero("Mes:")
                ano = self.entero("Año:")
                while date_valid == False:
                    if mes == 2 :
                        if ano % 4 == 0 :
                            if dia <= 29 and dia > 0 :
                                date_valid = True
                            else:
                                date_valid = False
                                print("repita la fecha")
                                break
                        elif ano % 4 != 0 :
                            if dia > 0 and dia <= 28 :
                                date_valid = True
                            else:
                                date_valid = False
                                print("repita la fecha")
                                break
                        else:
                            date_valid = False
                            print("repita la fecha")
                            break
                    elif mes <=7 :
                        if mes % 2 == 0 and dia > 0 and dia <= 30 :
                            date_valid = True
                        elif mes % 2 != 0 and dia > 0 and dia <= 31 :
                                date_valid = True
                        else:
                            date_valid = False
                            print("repita la fecha")
                            break
                    elif mes == 8 and dia > 0 and dia <= 31 :
                            date_valid = True
                    elif mes <=12 and mes > 8 :
                        if mes % 2 == 0 and dia > 0 and dia <= 31 :
                            date_valid = True
                        elif mes % 2 != 0 and dia > 0 and dia <= 30 :
                            date_valid = True
                        else:
                            date_valid = False
                            print("repita la fecha")
                            break
                    else :
                        date_valid = False
                        print("repita la fecha")
                        break
                    date.append((dia,mes,ano))# SI SE LE QUITAN UN TAB ENTONCES SIEMORE GUARDA LA FECHA 
                    break
            elif ELECCION == 2:
                return None
            return date
class eventoun :
    def __init__(self):
        self.evento = [] #necesito tener definido evento pero q no sea vacio
        self.cant_de_facturas = 0 ##   necesito q la cant de factura no se me ponga en 0 osea continuar con los eventos q tengo
    def agregar_factura(self):
        print("Selecciona el dia de la entrega\n")
        dias_de_venta = fechinguiri().fecha()
        from factura_PERFECTA import factura 
        if not dias_de_venta:
            print("Haga otra eleccion\n")
            return None
        if dias_de_venta[-1] == []:
                print("FECHA INCORRECTA")
        else :
            repetida = 0
            nueva_fecha = dias_de_venta[0]
            if repetida>=2:
                 print("Haz alcanzado el limite debes cambiar de dia")
            else:
                f = factura().go()
                if f == "Factura inválida":
                    return None
                else:
                    banana = {'fecha':nueva_fecha, 'factura': f }
                    self.evento.append(banana)
                    for e in self.evento:
                        if e['fecha'] == nueva_fecha:
                            repetida+=1
            return print("~~~~~~~FACTURA AÑADIDA CORRECTAMENTE~~~~~~~")
    def eliminar(self):
        while True:
            print("Estos son sus textos\n")
            eventoun().leer_texto()
            eliminar = input(f"Numero de la factura que desea eliminar (ESC : para volver):\n")
            if not eliminar.isdigit:
                print("Introduce un numero valido")
            elif eliminar == "ESC" or eliminar == "esc" :
                 break
            indice = int(eliminar)-1
            c = input(f"Este es su texto {self.evento[indice]["factura"]} (SI o NO):\n")
            if c.upper() == "SI":
                confirmacion = input(f"Seguro que desea eliminarlo:(SI o NO):\n")
                if confirmacion== "si" or confirmacion == "Si" or confirmacion == "SI" or confirmacion == "sI":
                    self.evento.pop(indice)
                    print("ELIMINANDO ...")
                    break
                else : 
                    confirmacion == "" or confirmacion !="SI"
                    print("RETORNAMOS")
            break
    def leer_texto(self):
        print("\n --- TUS TEXTOS GUARDADOS --- ")
        for u in enumerate (self.evento , start=1):#xq razon me esta poniendo la segunda nota igual a la primera
           print(u)
    def run(self):
        print("\n OPCIONES :")
        print("1. AGREGAR FACTURA")
        print("2. LEER FACTURAS")
        print("3. ELIMINAR FACTURA")
        print("4. SALIR")
        OPCION = input("ELIGE UNA OPCION:\n ")
        if OPCION == "1":
            self.agregar_factura()
            self.cant_de_facturas += 1
            return eventoun().run()
        elif OPCION == "2":
            self.leer_texto()
            return eventoun().run()
        elif OPCION == "3":
            self.eliminar()
            return eventoun().run()
        elif OPCION == "4":
            print("Saliendo ... ")
        else:
                print("Opcion inválida intente denuevo")
print(eventoun().run())