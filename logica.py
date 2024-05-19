import nodo

def contar_ocurrencias_caracteres(string):
    conteo = {}
    for caracter in string:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

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

def lista_enlazada_a_lista(cabeza):
    lista = []
    actual = cabeza
    while actual is not None:
        lista.append(actual)
        actual = actual.sig
    return lista

def ordenar_lista_asc(lista):
    menor = lista[0]
    i=1
    while lista[i] is not None: #arreglar
        if (lista[i].ocurrencia < menor.ocurrencia):
            aux = lista[i]
            lista[i] = menor
            menor = aux
        lista[i] = lista[i].sig


def imprimir_lista(lista):
    i=0
    while lista[i] is not None:
        print(f"Caracter: {lista[i].caracter}, Ocurrencia: {lista[i].ocurrencia}")
        lista[i] = lista[i].sig
