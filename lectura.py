import escritura

def leer_archivo_como_string(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"
    

def leer_diccionario_codigos(ruta_archivo):
    diccionario_codigos = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            caracter, codigo = linea.rstrip().split(':', 1)
            diccionario_codigos[codigo.strip()] = caracter
    return diccionario_codigos


def descomprimir_archivo(nombre_archivo_comprimido, nombre_archivo_salida, diccionario_codigos): #arreglar
    with open(nombre_archivo_comprimido, 'rb') as archivo:
        bits_relleno = archivo.read(1)[0]
        codigo_comprimido_bytes = archivo.read()
    
    codigo_comprimido_bits = escritura.bytes_a_bits(codigo_comprimido_bytes)
    
    # Eliminar los bits de relleno
    if bits_relleno:
        codigo_comprimido_bits = codigo_comprimido_bits[:-bits_relleno]
    
    # Leer diccionario de códigos
    diccionario_decodificacion = leer_diccionario_codigos(diccionario_codigos)
    print(diccionario_decodificacion)
    
    # Descomprimir el texto usando el diccionario de decodificación
    texto_decodificado = ""
    codigo_actual = ""
    for bit in codigo_comprimido_bits:
        codigo_actual += bit
        # Revisar si el código actual coincide con uno en el diccionario
        if codigo_actual in diccionario_decodificacion:
            caracter = diccionario_decodificacion[codigo_actual]
            texto_decodificado += caracter
            codigo_actual = ""
    
    # Guardar el texto descomprimido en un archivo de salida
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(texto_decodificado)

    print("Descompresión completada con éxito.")