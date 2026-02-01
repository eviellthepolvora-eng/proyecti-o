import json
class fechinguiri:
    def __init__(self):
        self.fecha = self.cargar_fechas()
    def entero(self,a):
        e = int(input(a))
        return e
    def date(self):
            date_valid = False
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
                date = dia,mes,ano# SI SE LE QUITAN UN TAB ENTONCES SIEMORE GUARDA LA FECHA 
                break
            return date
    def repeticion(self):
        for fechas in self.fechas:
            if fechas >=3:
                return "debe cambiar de dia"
            else:
                continue
    def guardar_fechas(self):
        with open("fechas.json", "w") as f: # w modificar archivo
            json.dump(self.fecha, f, indent=4)

    # Cargar desde archivo
    def cargar_fechas(self):
        try:
            with open("fechas.json", "r") as f: # r leer archivo
                return json.load(f)
        except FileNotFoundError:
            return []
    def brr(self):
        print("Este es su calendario")
        print("1 - Seleccione la fecha\n2 - Mostrar fechas de entrega\n3 - Desea volver atras")
        ELECCION = int(input("Elije una opcion\n"))
        if ELECCION == 1 :
            self.fecha = self.date()
            if self.repeticion():
                self.guardar_fechas(self.fecha)
        elif ELECCION == 2:
            print(self.fecha)
        elif ELECCION == 3:
             return None
#fechinguiri().brr()