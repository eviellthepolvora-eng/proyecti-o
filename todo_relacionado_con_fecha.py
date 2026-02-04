import json
from datetime import datetime, date

class fechinguiri:
    def __init__(self):
        self.fecha = self.cargar_fechas()   
    
    def es_bisiesto(self, ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    def entero(self,a):
        e = int(input(a))
        return e
    
    def validar_fecha(self):
        while True:
            while True:
                dia = self.entero("DIA :")
                if 1 <= dia <= 31:
                    print(f"Día válido: {dia}")
                    break
                else:
                    print("El día debe estar entre 1 y 31\n")
            while True:
                mes = self.entero("MES:")
                meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
                        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
                        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
                if 1 <= mes <= 12:
                    print(f"Mes válido: {mes} ({meses[mes]})")
                    break
                else:
                    print("El mes debe estar entre 1 y 12")
            while True:
                ano = self.entero("AÑO:")
                if 1900 <= ano <= 2100:
                    print(f"Año válido: {ano}")
                    break
                else:
                    print("El año debe estar entre 1900 y 2100")
            try:
                fecha = date(ano, mes, dia)
                print(f"FECHA COMPLETA: {fecha.strftime('%d/%m/%Y (%A)')}")
                confirmar = input("¿Es correcta esta fecha? (SI/NO): ").upper()
                if confirmar == "SI":
                    self.fecha.append(fecha)
                    self.guardar_fechas()
                    return fecha
                else:
                    print("\nVamos a ingresar la fecha nuevamente.\n")
            except ValueError as e:
                # Explicar específicamente qué está mal
                if mes == 2 and dia == 29 and not self.es_bisiesto(ano):
                    print(f"{ano} es un año bisiesto.")
                    print(f"El 29 de febrero solo existe en años bisiestos.")
                elif mes == 2:
                    print(f"{dia} no es un día válido para Febrero.")
                    if self.es_bisiesto(ano):
                        print(f"Febrero en {ano} tiene máximo 29 días.")
                    else:
                        print(f"Febrero en {ano} tiene máximo 28 días.")
                elif mes in [4, 6, 9, 11]:
                    print(f"{dia} no es un día válido.")
                    print(f"Este mes solo tiene 30 días.")
                else:
                    print(f"Fecha inválida. {str(e)}")
                print("Por favor, intente de nuevo.\n")
    def guardar_fechas(self):
        with open("fechas.json", "w") as f: # w modificar archivo
            json.dump(self.fecha, f, indent=4)
    def cargar_fechas(self):
        try:
            with open("fechas.json", "r") as f: # r leer archivo
                return json.load(f)
        except FileNotFoundError:
            return []
