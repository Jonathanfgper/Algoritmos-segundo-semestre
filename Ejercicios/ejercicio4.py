# Ejercicio 4
telefono = input("Introduce un número de teléfono en el formato +502-XXXXXXXX: ")

numero_sin_prefijo_y_extension = telefono.split('-')[1]

print(f"El número sin prefijo ni extensión es: {numero_sin_prefijo_y_extension}")
