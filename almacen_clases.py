#anadir la posibilidad de alerta cuando se acabe un modelo de moto
import json
class almacen :
    def __init__(self):
        self.CANTIDADES = []
        self.tabla = {}
        self.al = self.cargar_almacen()
        self.modelo = ["Yamaha" ,"Suzuki" , "AVA" , "Treck" , "Honda"]
    def almacenado(self):
        print("MOTOS EN EL ALMACEN\n")
        for i in self.modelo:
            cantidad = (input(f"Cantidad de {i} :"))
            self.CANTIDADES.append(int(cantidad))
        for fila in range(len(self.modelo)):
            self.tabla = {"modelo": self.modelo[fila], "cantidad": self.CANTIDADES[fila]}
            self.al.append(self.tabla)
        if len (self.al) > 1:
            self.al.pop() # usar del para eliminar el alamcen
            self.guardar_almacen()
        else:
            self.guardar_almacen()
        return print("INVENTARIO COMPLETO")
    def mostrar_vertical(self , a:dict):
        print("\nModelo".ljust(10), "|","Cantidad".rjust(10))
        for item in self.al:
            print("-"*24)
            print(f"{item['modelo'].ljust(10)} : {str(item['cantidad']).rjust(10)} ")
    def guardar_almacen(self):
        with open ("almacen.json" ,"w") as f:
            return json.dump(self.al , f, indent=4)
    def cargar_almacen(self):
        try:
            with open ("almacen.json" ,"r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def eliminacion_modelo (self):
        with open("entregado.json", "r") as f:
            z = json.load(f)
        if z == []:
            return print("No hay modelos para eliminar")
        modelo_a_eliminar = z[-1]
        for item in self.al:
            if item["modelo"] == modelo_a_eliminar["factura"]["modelo"]:
                item["cantidad"] = item["cantidad"] - modelo_a_eliminar["factura"]["CANTIDAD"]
                break
        self.guardar_almacen()
        return print("INVENTARIO ACTUALIZADO")

    def sin_stock(self):
        low = {}
        for item in self.al:
            if int(item.get("cantidad", 0)) <= 5:
                low[item.get("modelo")] = item.get("cantidad")
            continue
        return low
