import json
class fechinguiri:
    def __init__(self):
        self.fecha = self.cargar_fechas()
    def entero(self,a):
        e = int(input(a))
        return e
    def es_bisiesto(self, ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    def date(self):
            date_valid = False
            dia = self.entero("Dia:")
            mes = self.entero("Mes:")
            ano = self.entero("Año:")
            while date_valid == False:
                if mes == 2 :
                    if self.es_bisiesto(ano) :
                        if dia <= 29 and dia > 0 :
                            date_valid = True
                        else:
                            date_valid = False
                            print("repita la fecha")
                            break
                    if not self.es_bisiesto(ano):
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
                date = (dia,mes,ano)# SI SE LE QUITAN UN TAB ENTONCES SIEMORE GUARDA LA FECHA 
                break
            return date
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
    def incrementar_fecha(self, fecha):
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.es_bisiesto(fecha[2]):
            dias_por_mes[1] = 29
        fecha[0] += 1
        if fecha[0] > dias_por_mes[fecha[1] - 1]:
            fecha[0] = 1
            fecha[1] += 1
            if fecha[1] > 12:
                fecha[1] = 1
                fecha[2] += 1
        return tuple(fecha)    
    
