class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    def add_product(self, new_product):
        self.productos.append(new_product)
        return self

    def Print_info(self):
        print(f"El nombre de mi tienda es: {self.nombre} y tiene los siguientes productos:")
        for item in self.productos:
            item.Print_info()
    
    def sell_product(self, id):
        if id < len(self.productos):
            self.productos.pop(id)
        else:
            print("Este indice no existe")
    def __str__(self):
        return self.nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado == True:
            self.precio += self.precio *(cambio_porcentaje/100)
        else: 
            self.precio -= self.precio *(cambio_porcentaje/100)
    def Print_info(self):
        print(f"Nombre:{self.nombre} , Categoria:{self.categoria}, Precio:{self.precio}")
    

falaferia = Tienda(nombre = "falaferia")

cerveza = Producto(nombre = "cerveza", precio = 500, categoria = "bebestible")

falaferia.add_product(cerveza)
falaferia.add_product(Producto("Kross", 1990, "Bebestible"))

falaferia.Print_info()
falaferia.sell_product(0)

falaferia.Print_info()

