print("Programacion POO")
#definicion de clases
class perro:
    def morder(self):
        print("el perro me mordio")
    def datosperro(self,nombre,edad):
        print(f"Nombre: {nombre} Edad: {edad}")
#Zona de creacion
chihuahua=perro()
#Zona de uso de objetos
chihuahua.datosperro("Chopper",6)
chihuahua.morder()