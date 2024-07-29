import time

# Función de Búsqueda Lineal
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Función de Búsqueda Binaria
def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Función para medir el tiempo de ejecución
def medir_tiempo(func, lista, elemento):
    inicio = time.time()
    resultado = func(lista, elemento)
    fin = time.time()
    return resultado, fin - inicio

# Crear listas de diferentes tamaños
listas = {
    "10": list(range(10)),
    "100": list(range(100)),
    "1000": list(range(1000)),
    "10000": list(range(10000))
}

# Elemento a buscar (último elemento para peor caso)
elemento = -1  # Un elemento que no está en la lista para asegurar el peor caso

# Comparar tiempos de búsqueda lineal y binaria
for tamano, lista in listas.items():
    resultado_lineal, tiempo_lineal = medir_tiempo(busqueda_lineal, lista, elemento)
    resultado_binaria, tiempo_binaria = medir_tiempo(busqueda_binaria, lista, elemento)

    print(f"Tamaño de la lista: {tamano}")
    print(f"  Búsqueda Lineal - Índice: {resultado_lineal}, Tiempo: {tiempo_lineal:.10f} segundos")
    print(f"  Búsqueda Binaria - Índice: {resultado_binaria}, Tiempo: {tiempo_binaria:.10f} segundos")
    print()
