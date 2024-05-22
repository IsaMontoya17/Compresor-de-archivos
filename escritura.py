import lectura

def generar_guardar_diccionario_codigos(codigos_huffman):
    diccionario_codigos = {item[0]: item[2] for item in codigos_huffman}
    ruta_archivo = "./archivos/diccionarioCodigos.txt"

    with open(ruta_archivo, 'w') as archivo:
        for caracter, codigo in diccionario_codigos.items():
            archivo.write(f"{caracter}: {codigo}\n")

def comprimir_texto(texto, ruta_diccionario_codigos):
    # Leer el diccionario de códigos desde el archivo
    diccionario_codigos = lectura.leer_diccionario_codigos(ruta_diccionario_codigos)

    # Invertir el diccionario para que las claves sean los caracteres y los valores sean los códigos
    diccionario_codigos = {valor: clave for clave, valor in diccionario_codigos.items()}

    try:
        # Generar el código comprimido para el texto
        codigo_comprimido = ''.join(diccionario_codigos[caracter] if caracter != '\n' else diccionario_codigos['\\n'] for caracter in texto)
    except KeyError as e:
        raise ValueError(f"El carácter '{e.args[0]}' no tiene un código asignado.") from e

    # Calcular los bits de relleno
    bits_relleno = (8 - len(codigo_comprimido) % 8) % 8

    # Agregar bits de relleno al final
    codigo_comprimido += '0' * bits_relleno

    return codigo_comprimido, bits_relleno


def escribir_archivo_comprimido(nombre_archivo, codigo_comprimido_bytes, bits_relleno):
    with open(nombre_archivo, 'wb') as archivo:
        # Escribir la cantidad de bits de relleno como el primer byte
        archivo.write(bytes([bits_relleno]))
        archivo.write(codigo_comprimido_bytes)

def bits_a_bytes(bits):
    # Convertir la secuencia de bits en una lista de bytes
    bytes_list = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]
    
    # Convertir la lista de bytes en un objeto bytes
    return bytes(bytes_list)

def bytes_a_bits(byte_data):
    # Convierte bytes a una cadena de bits
    return ''.join(format(byte, '08b') for byte in byte_data)

