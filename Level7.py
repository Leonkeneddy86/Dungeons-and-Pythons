def decodificar_manuscrito(texto):
    return str([ord(letra) for letra in texto if letra != ' '])