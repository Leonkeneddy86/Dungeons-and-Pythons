def identificar_numeros_magicos(lista):
    return str([num for num in lista if num % 3 == 0 and num % 5 != 0])
    pass
