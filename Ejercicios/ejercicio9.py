# Ejercicio 9
fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, anio = fecha_nacimiento.split('/')

print(f"Día: {int(dia)}, Mes: {int(mes)}, Año: {anio}")
