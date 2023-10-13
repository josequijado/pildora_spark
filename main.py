# Importar las bibliotecas de PySpark
from pyspark import SparkConf, SparkContext

import logging
logger = logging.getLogger("py4j")
logger.setLevel(logging.ERROR)

# Configurar Spark
conf = SparkConf().setAppName("ConteoPalabras")
sc = SparkContext(conf=conf)

# Cargar el archivo de texto en un RDD (Resilient Distributed Dataset)
archivo = "texto.txt"
lines = sc.textFile(archivo)

lineas = lines.collect()
for line in lineas:
    print (f"LINEA: {line}")

# Dividir cada línea en palabras
words = lines.flatMap(lambda line: line.split(" "))

# Asignar un valor de 1 a cada palabra
word_counts = words.map(lambda word: (word, 1))

# Sumar el valor de 1 para cada palabra
word_counts = word_counts.reduceByKey(lambda a, b: a + b)

# Mostrar los resultados
resultado = word_counts.collect()
for palabra, conteo in resultado:
    print(f"{palabra}: {conteo}")

# Detener Spark
sc.stop()
