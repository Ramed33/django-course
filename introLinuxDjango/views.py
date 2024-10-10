from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

class Ubicacion:

    def __init__(self, departamento, seccion, subseccion):
        self.departamento = departamento
        self.seccion = seccion
        self.subseccion = subseccion
        print("El departamento, la sección, la subsección y la ubicación se han creado correctamente")

    def print_departamento(self):
        print("El departamento creado es: {}".format(self.departamento))

    def print_seccion(self):
        print("La seccion creada es: {}".format(self.seccion))

    def print_subseccion(self):
        print("La subsección creada es: {}".format(self.subseccion))

    def print_ubicacion(self):
        print(" La ubicación del artículo es:\n Departamento: {} \n Sección: {}\n Subsección: {}".format(self.departamento, self.seccion, self.subseccion))

class Articulo(Ubicacion):

    def __init__(self, departamento, seccion, subseccion, nombre, marca, precio):
        super().__init__(departamento, seccion, subseccion)
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        print("El nombre, marca y precio del artículo se han creado correctamente")

    def print_article(self):
        print(" El artículo se encuentra en:\n El departamento de {} \n La sección es {}\n La subsección es {}\n El nombre es {}\n La marca es {}\n El precio es {}".format(self.departamento, self.seccion, self.subseccion, self.nombre, self.marca, self.precio))

def item(request):

    jersey_liverpool = Articulo("Deportes", "Ropa", "Jerseys", "Liverpool", "Nike", "1300")

    doc_ext = open("introLinuxDjango/cart.html")

    plt = Template(doc_ext.read())

    doc_ext.close()

    ctx = Context({"item_departamento":jersey_liverpool.departamento, "item_seccion":jersey_liverpool.seccion, "item_subseccion":jersey_liverpool.subseccion, "item_nombre":jersey_liverpool.nombre, "item_marca":jersey_liverpool.marca, "item_precio":jersey_liverpool.precio})

    document = plt.render(ctx)

    return HttpResponse(document)