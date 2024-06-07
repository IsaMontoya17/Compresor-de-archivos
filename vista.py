import lectura, escritura, logica

nombre_archivo = "./archivos/prueba.txt"
nombre_archivo_comprimido = "./archivos/comprimido.txt"
nombre_archivo_descomprimido = "./archivos/descomprimido.txt"
nombre_diccionario_codigos = "./archivos/diccionarioCodigos.txt"

def comprimir_archivo():
    
    texto = lectura.leer_archivo_como_string(nombre_archivo)
    if "El archivo no fue encontrado." in texto or "Ocurrió un error" in texto:
        print(texto)
        return

    conteo = logica.contar_ocurrencias_caracteres(texto)
    cabeza = logica.convertir_a_lista_nodos(conteo)
    cabeza = logica.ordenar_lista_asc(cabeza)
    arbol_huffman = logica.generar_arbol_huffman(cabeza)
    codigos_huffman = []
    logica.asignar_codigos_huffman(arbol_huffman, "", codigos_huffman)

    escritura.generar_guardar_diccionario_codigos(codigos_huffman)
    codigo_comprimido, bits_relleno = escritura.comprimir_texto(texto, nombre_diccionario_codigos)
    codigo_comprimido_bytes = escritura.bits_a_bytes(codigo_comprimido)
    escritura.escribir_archivo_comprimido(nombre_archivo_comprimido, codigo_comprimido_bytes, bits_relleno)
    
    print("Compresión completada con éxito.")

def descomprimir_archivo():
    
    lectura.descomprimir_archivo(nombre_archivo_comprimido, nombre_archivo_descomprimido, nombre_diccionario_codigos)
    
    print("Descompresión completada con éxito.")

def main():
    opcion_1_ejecutada = False
    opcion_2_ejecutada = False

    while True:
        if not opcion_1_ejecutada and not opcion_2_ejecutada:
            print("Bienvenido")
        print("\n" + "¿Qué acción desea realizar?")
        if not opcion_1_ejecutada:
            print("1. Comprimir archivo")
        if opcion_1_ejecutada:
            print("2. Descomprimir archivo")

        opcion = input("\n" + "Ingrese el número de la acción que desea realizar: ")

        if opcion == "1":
            comprimir_archivo()
            opcion_1_ejecutada = True
        elif opcion == "2" and opcion_1_ejecutada:
            opcion_2_ejecutada = True
            if lectura.verificar_existencia_archivo(nombre_archivo_comprimido):
                descomprimir_archivo()
            else:
                print("\n" + "No se puede descomprimir porque el archivo comprimido no existe.")
        else:
            print("\n" +"Opción inválida. Por favor, ingrese 1 o 2.")

        if opcion_1_ejecutada and not opcion_2_ejecutada:
            continuar = input("\n" + "¿Desea realizar otra acción? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            break
