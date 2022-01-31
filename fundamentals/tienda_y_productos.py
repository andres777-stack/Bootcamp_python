class Tienda:
    def __init__(self, name, productos = []):
        self.name = name
        self.productos = productos
    def add_product(self, new_product, precio, categoria):
        self.productos.append(Producto(nombre = new_product, precio = precio, categoria = categoria))
        return self
    def sell_product(self, id):
        print("Producto vendido: ", self.productos[id].nombre)
        self.productos.remove(self.productos[id])
        return self
    def inflation(self, percent_increase):
        for i in self.productos:
            increase = i.precio * percent_increase
            i.precio += increase
            return self

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            percent_variation = self.precio * percent_change
            self.precio += percent_variation
            return self
        else:
            percent_variation = self.precio * percent_change
            self.precio -= percent_variation
            return self
    def print_info(self):
        print(self.nombre, self.precio, self.categoria)



i = Producto(nombre = "arroz", precio = 100, categoria = "alimento")

print(i.precio)

i.update_price(0.10, True)
print(i.precio)
shop = Tienda(name = "Barberia")
print(shop.name)
shop.add_product(new_product = "Cerveza", precio = 100, categoria = "Alcohol")
shop.add_product(new_product = "Arroz", precio = 50, categoria = "Grano")
shop.add_product(new_product = "pulpa", precio = 200, categoria = "Carne")
print(len(shop.productos))
print(shop.productos[0].nombre)
shop.sell_product(0)
print(len(shop.productos))
shop.productos[0].print_info()
shop.productos[1].update_price(0.05, is_increased = True).print_info()
shop.inflation(0.10)
shop.productos[0].print_info()

