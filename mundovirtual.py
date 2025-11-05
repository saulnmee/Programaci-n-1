print("Bienvenido al mundo de los videojuegos")

info_tienda = ("Mas que un juego, una vida", 2025)

inventario = {
    "Fortine": {"precio":400,"stock":15},
    "Fifa 26": {"precio":1100,"stock":10},
    "Sekiro": {"precio": 700,"stock":7}, 
}

print(inventario["Fifa 26"]["precio"])

print("Vendiste la copia del juego")

inventario["Fortnite"]["stock"]= 14
print(inventario["Fortnite"])

print("Lista actualizada")