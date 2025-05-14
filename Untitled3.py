import random
import os


resultados = random.sample(range(0, 46), 6)
print("3) Resultados del Quini 6:")
print("Números sorteados:", resultados)


try:
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados del Quini 6:\n")
        archivo.write(", ".join(map(str, resultados)))
    print("\nArchivo 'resultados.txt' generado con éxito.")
except Exception as e:
    print("Error al guardar resultados.txt:", e)


archivo_lenguajes = "lenguajes.txt"


if not os.path.exists(archivo_lenguajes):
    open(archivo_lenguajes, "w").close()

