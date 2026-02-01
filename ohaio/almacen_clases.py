#anadir la posibilidad de alerta cuando se acabe un modelo de moto
class almacen :
    def __init__(self):
        self.CANTIDADES = []
        self.tabla = {}
        self.modelo = ["Yamaha" ,"Suzuki" , "AVA" , "Treck" , "Honda"]
    def almacenado(self):
        print("MOTOS EN EL ALMACEN\n")
        for i in self.modelo:
            cantidad = (input(f"Cantidad de {i} :"))
            self.CANTIDADES.append(cantidad)
        for fila in range(len(self.modelo)):
            self.tabla[self.modelo[fila]] = self.CANTIDADES[fila]
        return "INVENTARIO COMPLETO"
    def mostrar_vertical(self , a:dict):
        print("\nModelo".ljust(10), "|","Cantidad".rjust(10))
        for modelo , cantidad in self.tabla.items():
            print("-"*24)
            print(f"{modelo.ljust(10)} : {cantidad.rjust(10)} ")

#a = almacen()
#a.almacenado()
#print(a.mostrar_vertical(a.tabla))
#verificacion de la existencia del modelo de moto
# factura[0] indice de modelo de moto

#cantidad = [23 , 42 , 56, 33 ,13]#Yamaha #Suzuki #AVA #Treck #Honda
#almacen = [[modelo[0]*cantidad[0]] ,[modelo[1]*cantidad[1]] ,[modelo[2]*cantidad[2]] ,[modelo[3]*cantidad[3]] ,[modelo[4]*cantidad[4]]] 


#def Yamaha:
#    return modelo[0] | (CANTIDADES[0])
#
#def Suzuki :
#    return modelo[1] | (CANTIDADES[1])
#
#def AVA
#    return modelo[2] | (CANTIDADES[2])
#
#def Treck
#    return modelo[3] | (CANTIDADES[3])
#
#def Honda
#    return modelo[4] | (CANTIDADES[4])