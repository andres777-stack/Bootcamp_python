def monedas(numero):
    monedas = [25, 10, 5, 1]
    cantidad = []
    for moneda in monedas:
        cantidad.append(int(numero/moneda))
        numero -= ((int(numero/moneda)) * moneda)
    return cantidad

print(monedas(430))