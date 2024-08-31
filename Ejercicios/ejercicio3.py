# Ejercicio 3
nombre = input("Introduce tu nombre: ")
nombre_mayusculas = nombre.upper()
numero_letras = len(nombre.replace(" ", ""))  # Excluye los espacios del conteo de letras

print(f"{nombre_mayusculas} tiene {numero_letras} letras.")
