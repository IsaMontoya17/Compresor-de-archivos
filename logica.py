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
def ordenar_lista_asc(cabeza):
    if cabeza is None or cabeza.sig is None:
        return cabeza

    # Convertir la lista enlazada a una lista estándar
    lista = lista_enlazada_a_lista(cabeza)

    # Ordenar la lista de forma ascendente
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j].ocurrencia > lista[j+1].ocurrencia:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    # Actualizar los enlaces sig en la lista enlazada original
    for i in range(n-1):
        lista[i].sig = lista[i+1]
    lista[-1].sig = None

    return lista[0]

def insertar_ordenado(cabeza, nuevo_nodo):
    if cabeza is None or nuevo_nodo.ocurrencia < cabeza.ocurrencia:
        nuevo_nodo.sig = cabeza
        return nuevo_nodo

    actual = cabeza
    while actual.sig is not None and actual.sig.ocurrencia <= nuevo_nodo.ocurrencia:
        actual = actual.sig

    nuevo_nodo.sig = actual.sig
    actual.sig = nuevo_nodo

    return cabeza

def generar_arbol_huffman(cabeza):
    contador = 1
    while cabeza and cabeza.sig:
        primero = cabeza
        segundo = cabeza.sig

        nuevo_caracter = f"*{contador}"
        nuevo_nodo = nodo.nodo(nuevo_caracter, primero.ocurrencia + segundo.ocurrencia)
        nuevo_nodo.der = primero
        nuevo_nodo.izq = segundo

        cabeza = segundo.sig
        cabeza = insertar_ordenado(cabeza, nuevo_nodo)
        contador += 1

    return cabeza

# Función para imprimir la lista
def imprimir_lista(cabeza):
    actual = cabeza
    while actual is not None:
        print(f"Caracter: {actual.caracter}, Ocurrencia: {actual.ocurrencia}, dir: {actual}, sig: {actual.sig}")
        actual = actual.sig