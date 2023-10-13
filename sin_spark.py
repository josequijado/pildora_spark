import itertools
import string
from collections import Counter

# Nombre del archivo de texto
archivo = "texto.txt"

palabras = []
with open(archivo, "r") as file:
    for line in file:
        palabras.append(line.split())

palabras = list(itertools.chain.from_iterable(palabras))
palabras = [palabra.lower() for palabra in palabras]

# Eliminar los signos de puntuación
palabras = [palabra.translate(str.maketrans('', '', string.punctuation)) for palabra in palabras]

conteo = Counter(palabras)

for elemento, veces in conteo.items():
    print (elemento, ":", veces)


# Crear una tabla de traducción para reemplazar letras mayúsculas con números y eliminar signos de puntuación
tabla = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '12345678901234567890123456', string.punctuation)

# Cadena de origen
cadena = "¡Hola, Mundo! Este es un Ejemplo."
56
# Aplicar la traducción
cadena_transformada = cadena.translate(tabla)

print(cadena_transformada)  # Resultado: "¡123a, 456u7890 123e5 67 12345670"