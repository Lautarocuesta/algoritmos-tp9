def busqueda_lineal(lista, elemento):

    for i in range(len(lista)):
           if lista[i] == elemento:
            return i
    return -1

    """
    Realiza una búsqueda lineal en una lista.
    
    Parámetros:
    lista (list): Lista en la que buscar el elemento.
    elemento (any): Elemento a buscar en la lista.
    
    Retorna:
    int: Índice del elemento si se encuentra en la lista, -1 si no está presente.
    """