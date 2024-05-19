import lectura, logica, escritura, nodo

def main():
    contenido = lectura.leer_archivo_como_string('./archivos/prueba.txt')
    print(contenido)

    conteo = logica.contar_ocurrencias_caracteres(contenido)
    print(conteo)
    
    lista_nodos = logica.convertir_a_lista_nodos(conteo)
    lista = logica.lista_enlazada_a_lista(lista_nodos)
    logica.ordenar_lista_asc(lista)
    logica.imprimir_lista(lista)

if __name__ == "__main__":
    main()