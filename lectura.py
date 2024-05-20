def leer_archivo_como_string(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"

def generar_diccionario_decodificacion(codigos_huffman):
    diccionario = {}
    for tupla in codigos_huffman:
        caracter, codigo = tupla[0], tupla[2]
        diccionario[codigo] = caracter
    return diccionario

def descomprimir_texto(codigo_comprimido, diccionario_decodificacion):
    codigo_actual = ""
    texto_descomprimido = ""
    
    for bit in codigo_comprimido:
        codigo_actual += bit
        if codigo_actual in diccionario_decodificacion:
            texto_descomprimido += diccionario_decodificacion[codigo_actual]
            codigo_actual = ""
    
    return texto_descomprimido

def escribir_archivo_descomprimido(nombre_archivo, texto_descomprimido):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto_descomprimido)
