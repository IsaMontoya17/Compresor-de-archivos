import lectura, logica, escritura

def main():
    nombre_archivo = "./archivos/prueba.txt"
    nombre_archivo_comprimido = "./archivos/comprimido.txt"
    nombre_archivo_salida = "./archivos/descomprimido.txt"
    nombre_diccionario_codigos = "./archivos/diccionarioCodigos.txt"
    
    texto = lectura.leer_archivo_como_string(nombre_archivo)
    if "El archivo no fue encontrado." in texto or "Ocurrió un error" in texto:
        print(texto)
        return

    # Contar ocurrencias
    conteo = logica.contar_ocurrencias_caracteres(texto)
    
    # Convertir a lista enlazada de nodos
    cabeza = logica.convertir_a_lista_nodos(conteo)
    
    # Ordenar lista de nodos
    cabeza = logica.ordenar_lista_asc(cabeza)
    
    # Generar árbol Huffman
    arbol_huffman = logica.generar_arbol_huffman(cabeza)
    
    # Asignar códigos Huffman
    codigos_huffman = []
    logica.asignar_codigos_huffman(arbol_huffman, "", codigos_huffman)
    
    print("Códigos Huffman asignados:")
    for caracter, ocurrencia, codigo, longitud in codigos_huffman:
        print(f"Caracter: {caracter}, Ocurrencia: {ocurrencia}, Codigo: {codigo}, Longitud: {longitud}")

    # Generar diccionario de códigos
    diccionario_codigos = escritura.generar_diccionario_codigos(codigos_huffman)
    escritura.guardar_diccionario_codigos(codigos_huffman)
    
    # Comprimir texto
    codigo_comprimido, bits_relleno = escritura.comprimir_texto(texto, diccionario_codigos)
    print(codigo_comprimido)
    
    # Convertir el código comprimido a bytes
    codigo_comprimido_bytes = escritura.bits_a_bytes(codigo_comprimido)
    
    # Escribir archivo comprimido
    escritura.escribir_archivo_comprimido(nombre_archivo_comprimido, codigo_comprimido_bytes, bits_relleno)
    
    print("Compresión completada con éxito.")

    # Descomprimir archivo

    lectura.descomprimir_archivo(nombre_archivo_comprimido, nombre_archivo_salida, nombre_diccionario_codigos)
    
if __name__ == "__main__":
    main()
