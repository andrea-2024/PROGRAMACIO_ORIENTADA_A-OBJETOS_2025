''' POLIMORFISMO DE FUNCION, DE MANERA EXTERNA
PODEMOS TRABAJAR LAS DIFERENTES CLASES Y LAMAR
 CUANDO SE REQUIERA LA INFORMACION'''

class Tomate:      #creamos una clase
    def tipo(self): #creamos el metodo
        print("verdura") #print para visualizar

    def color(self):     #creamos otro metodo
        print("rojo")

#creamos una segunda clase
#tomamos en cuenta algo que tengan en comun
#pero a la vez distintos

class Manzana:
    def tipo(self):
        print("fruta")

    def color(self):
        print("verde")
#creamos una funcion externa
#Esta funcion trabaja de manera directa con los diferentes metodos que tiene cada clase
def funcion(objeto):  #creamos los propios elementos
    objeto.tipo()        #creamos los atributos a cada accion
    objeto.color()

#creamos un objeto

nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nueva_manzana= Manzana()
funcion(nueva_manzana)
