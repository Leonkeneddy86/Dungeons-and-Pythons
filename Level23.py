def descifrar_codigo(codigo_cifrado):
    return "".join(chr(int(num) + 64) for num in codigo_cifrado.split(","))
    pass
