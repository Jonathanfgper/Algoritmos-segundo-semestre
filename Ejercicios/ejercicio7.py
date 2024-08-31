# Ejercicio 7
correo = input("Introduce tu correo electrónico: ")

nombre_usuario = correo.split('@')[0]

nuevo_correo = f"{nombre_usuario}@edu.gt"

print(f"Tu nuevo correo electrónico es: {nuevo_correo}")
