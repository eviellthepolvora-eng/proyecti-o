class factura:
    def __init__(self):
        self.factura = {"MODELO": None,
                        "CANTIDAD":None,
                        "DIRECCION":None,
                        "CLIENTE": None,
                        "TELEFONO": None,
                        "CUÑO":None
                        }
    def modelo(self):
        modelos = ["Yamaha" ,"Suzuki" , "AVA" , "Treck" , "Honda"]
        print("Estos son los modelos disponibles")
        for i, m in enumerate(modelos):
            print(f"{i} = {m}")
        while True:
            eleccion =int(input(f"Escoje el modelo\n"))
            #if not eleccion.isdigit() :
            #    print("Introduzca un numero valido")
            #    continue
            if 0 <= eleccion < len(modelos): 
                self.factura["MODELO"] = modelos[eleccion]
                cant = int(input("Cuantas motos deseas :\n"))
                if not cant:
                    self.factura["CANTIDAD"] = 1
                else:
                    self.factura["CANTIDAD"] = cant
            else:
                print("Introduzca un numero valido")
                return None
            return modelos[eleccion] , cant
    def direccion(self):
        provincia = input("Provincia:\n")
        municipio = input("Municipio:\n")
        calle =  input("Calle:\n")
        entrecalle = (input("entre :\n") , input("y :\n"))
        lugar = input("Vives en casa o edificio:\n")
        num_ok = None
        if not calle or not entrecalle or not municipio or not provincia:
            print("Factura inválida")
            return None
        if lugar == "edificio":
            num_edif = input("Número del edificio:\n")
            if not num_edif.isdigit() :
                print("Factura inválida")
                return None
            apto = input("Número del apartamento:\n")
            if apto[-1].isalpha() and apto[-1].upper()>="J":
                print("Factura inválida , ese apartamrnto no existe")
                return None
            if not apto:
                print("Factura inválida")
                return None
            num_ok = f" Edificio: {num_edif}, Apto :{apto}"
        elif lugar == "casa":
            num_casa = input("Número de la casa:\n")
            if num_casa[-1].isalpha() and num_casa[-1].upper()>="D":
                print("Factura inválida , esa casa no existe")
                return None
            if not num_casa :
                print("Factura inválida , esa casa no existe")
                return None
            num_ok = f" Casa: {num_casa}"
        else:
            print("Factura inválida")
            return None
        self.factura["DIRECCION"] = (provincia , municipio ,calle , entrecalle , num_ok)
        return self.factura["DIRECCION"]
    def nombre_del_cliente(self):
        first_name = input("Primer nombre :\n")
        second_name = input("Segundo nombre :\n")
        if not first_name or first_name.isdigit() :
            print("Factura invalida")
            return None
        primer_apellido = (input("Primer apellido :\n"))
        segundo_apellido = (input("Segundo apellido :\n"))
        if (not primer_apellido and not segundo_apellido) or (not primer_apellido) or (not segundo_apellido): 
            print("Factura invalida")
            return None
        elif (primer_apellido.isdigit() or segundo_apellido.isdigit()) :
            print("Factura invalida")
            return None
        self.factura["CLIENTE"] = (f"Nombre : {first_name , second_name} , Apellidos : {primer_apellido , segundo_apellido}")
        return self.factura["CLIENTE"]
    def telefono(self):
        numero = (input("Introduce el telefono del cliente:\n"))
        if len(numero) != 8 or not numero.isdigit():
            print ("Repita el numero , Factura inválida")
            return None
        codigo_pais = input("Introduzca el codigo de su país :\n")
        if not codigo_pais.startswith('+'):
            telefono_Ok = (f"+{codigo_pais} {numero}")
            self.factura["TELEFONO"] = telefono_Ok
            return self.factura["TELEFONO"] 
        else : 
            telefono_Ok = (codigo_pais + numero)
            self.factura["TELEFONO"] = telefono_Ok
            return self.factura["TELEFONO"] 
    def cuño(self):
        cuño = input("Cuño de pagado : (SI O NO) : \n").upper()
        if cuño == "SI" :
            self.factura["CUÑO"] =" PAGADO "
            print("El cuño ha sido agregado a la factura , listo para entregar al almacenero")
        else : 
            not cuño or cuño !="SI"
            print("Factura inválida")
            return None
        return "PAGADO"
    def verificacion(self , resultado, nombre="metodo"):# resultado es si da return none
        if resultado is None:
            print(f"{nombre} no se ha completado correctamente")
            return False
        return True
    def go(self):
        print("~~~~~~~Factura del cliente~~~~~~~")
        res = self.modelo()
        #anadir una restriccion tal que si quedan 5 motos o menos en el almacen "ALERTA DE STOCK BAJO"
        if not self.verificacion(res , "modelo"):
            return None
        res = self.direccion()
        if not self.verificacion(res , "direccion"):
            return None
        res = self.nombre_del_cliente()
        if not self.verificacion(res , "nombre_del_cliente"):
            return None
        res = self.telefono()
        if not self.verificacion(res , "telefono"):
            return None
        res = self.cuño()
        if not self.verificacion(res , "cuño"):
            return None
        print ("\nfactura lista")
        return self.factura
    
#a = factura()
#print(a.go())