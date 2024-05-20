def generar_diccionario_codigos(codigos_huffman):
    diccionario = {}
    for tupla in codigos_huffman:
        caracter, codigo = tupla[0], tupla[2]  # tupla[0] es el caracter, tupla[2] es el codigo
        diccionario[caracter] = codigo
    return diccionario

def comprimir_texto(texto, diccionario_codigos):
    try:
        codigo_comprimido = ''.join(diccionario_codigos[caracter] for caracter in texto)
    except KeyError as e:
        raise ValueError(f"El carácter '{e.args[0]}' no tiene un código asignado.") from e

    # Asegurarnos de que el código comprimido tenga una longitud múltiplo de 8
    while len(codigo_comprimido) % 8 != 0:
        codigo_comprimido += '0'
    return codigo_comprimido

def escribir_archivo_comprimido(nombre_archivo, codigo_comprimido):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(codigo_comprimido)
        
def escribir_archivo_descomprimido(nombre_archivo, texto_descomprimido):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto_descomprimido)