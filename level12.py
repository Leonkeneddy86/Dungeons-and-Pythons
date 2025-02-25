def encontrar_objeto_legendario(objetos):
    if not objetos:
        return ""
    return str(max(objetos, key=lambda x: x[1]))
