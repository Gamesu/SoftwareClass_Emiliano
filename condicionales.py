# Explicacion de condicionales

# Funcion para recibir datos desde consola
# input()
# int()

# Operadores Logicos
# ==, <, >, <=, >= // or, and

'''
# =========================================
camisa = 1

if camisa == 1: # Expresion Logica
    # Sentencia o acciona ejecutar si se cumple la expresion logica
    print("Tiene la camisa negra")

print("\nFin del programa")

# =========================================
camisa = 0

if camisa == 1: # Expresion Logica
    # Sentencia o acciona ejecutar si se cumple la expresion logica
    print("Tiene la camisa negra")
else:
    print("Tiene la camisa de otro color")

print("\nFin del programa")
'''
# =========================================
# 45 - 55 años validar si se puede vacunar por la edad
edad = int(input("Por favor ingrese su edad: "))
# 2 forma //edad = int(input("Por favor ingrese su edad"))
# 1 forma // edad = int(edad)

# Validar la edad
# 3 forma // if int(edad) >= 45 and int(edad) <= 55:
if edad >= 45 and edad <= 55:
    print("La persona se puede vacunar")
else:
    print("La persona NO se puede vacunar aun")
