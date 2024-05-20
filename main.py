import lectura, logica, escritura, nodo

def main():
    nombre_archivo = "./archivos/prueba.txt"
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
    
    print("Codigos Huffman asignados:")
    for caracter, ocurrencia, codigo, longitud in codigos_huffman:
        print(f"Caracter: {caracter}, Ocurrencia: {ocurrencia}, Codigo: {codigo}, Longitud: {longitud}")

    
    # Generar diccionario de códigos
    diccionario_codigos = escritura.generar_diccionario_codigos(codigos_huffman)
    
    # Comprimir texto
    codigo_comprimido = escritura.comprimir_texto(texto, diccionario_codigos)
    print(codigo_comprimido)
    
    # Escribir archivo comprimido
    escritura.escribir_archivo_comprimido("./archivos/comprimido.txt", codigo_comprimido)
    
    print("Compresión completada con éxito.")
    
    # Descompresión
    
    # Leer el código comprimido desde el archivo
    codigo_comprimido_leido = lectura.leer_archivo_como_string("./archivos/comprimido.txt")
    
    # Generar diccionario de decodificación
    diccionario_decodificacion = lectura.generar_diccionario_decodificacion(codigos_huffman)
    
    # Descomprimir texto
    texto_descomprimido = lectura.descomprimir_texto(codigo_comprimido_leido, diccionario_decodificacion)
    
    # Escribir archivo descomprimido como texto
    escritura.escribir_archivo_descomprimido("./archivos/descomprimido.txt", texto_descomprimido)
    
    print("Descompresión completada con éxito.")
    
if __name__ == "__main__":
    main()