import lectura, logica, escritura, nodo

def main():
    contenido = lectura.leer_archivo_como_string('./archivos/prueba.txt')
    print(contenido)

    conteo = logica.contar_ocurrencias_caracteres(contenido)
    print(conteo)
    
    lista_nodos = logica.convertir_a_lista_nodos(conteo)
    cabeza = logica.ordenar_lista_asc(lista_nodos)
    logica.imprimir_lista(cabeza)
    
    arbol_huffman = logica.generar_arbol_huffman(cabeza)
    
    print("Árbol de Huffman generado:")
    logica.imprimir_lista(arbol_huffman)

if __name__ == "__main__":
    main()