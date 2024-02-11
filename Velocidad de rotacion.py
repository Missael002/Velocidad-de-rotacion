# Definición de la función factorial para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Definición de la función coseno para calcular una aproximación del coseno de un ángulo
def coseno(x, n):
    cos_x = 0
    for i in range(n):
        coeficiente = (-1) ** i
        numerador = x ** (2 * i)
        denominador = factorial(2 * i)
        cos_x += coeficiente * (numerador / denominador)
    return cos_x

latitud = float(input("Introduce el valor de la Latitud: "))

# Ángulo en radianes (convertir la latitud de grados a radianes)
angulo_radianes = latitud * (3.14159 / 180)

# Número de términos en la serie de Maclaurin
num_terminos = 20

# Calcular el coseno de la latitud utilizando la serie de Maclaurin
resultado = coseno(angulo_radianes, num_terminos)

#Aplicar la formula
r = 0.0000729 * 6371000 * resultado

# Convertir la velocidad de metros por segundo a kilómetros por hora
v = r * 3.6  

print("El resultado es: ", v, "km/h")
