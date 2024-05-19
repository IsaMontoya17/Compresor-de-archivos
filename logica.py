import nodo

def contar_ocurrencias_caracteres(string):
    conteo = {}
    for caracter in string:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

# Función para convertir el conteo a una lista enlazada de nodos
def convertir_a_lista_nodos(conteo):
    cabeza = None
    actual = None
    for caracter, ocurrencia in conteo.items():
        nuevo_nodo = nodo.nodo(caracter, ocurrencia)
        if cabeza is None:
            cabeza = nuevo_nodo
            actual = nuevo_nodo
        else:
            actual.sig = nuevo_nodo
            actual = nuevo_nodo
    return cabeza

# Función para convertir una lista enlazada a una lista estándar
def lista_enlazada_a_lista(cabeza):
    lista = []
    actual = cabeza
    while actual is not None:
        lista.append(actual)
        actual = actual.sig
    return lista

# Función para ordenar una lista de nodos en orden ascendente por ocurrencia
def ordenar_lista_asc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j].ocurrencia > lista[j+1].ocurrencia:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Función para imprimir una lista de nodos
def imprimir_lista(lista):
    for nodo in lista:
        print(f"Caracter: {nodo.caracter}, Ocurrencia: {nodo.ocurrencia}")
