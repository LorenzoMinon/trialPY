class Cliente():

    def __init__(self,name,dni,mail,adress):
        self.name = input("Ingrese nombre: ")
        self.dni = input("Ingrese dni: ")
        self.mail = input("Ingrese mail: ")
        self.adress = input("Ingrese dirección: ")


    def __str__(self):
        cadena = "Bienvenido "+ self.name +" !! , DNI N°: "+self.dni+", su dirección de correo es: "+self.mail+" con domicilio en: "+self.adress
        return cadena


    def comprar_item(self,item):
        self.item = input("Ingrese el producto que desea comprar: ")
        
        print(f"Usted a comprado un {self.item}")


