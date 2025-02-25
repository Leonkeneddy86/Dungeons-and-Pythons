def contar_vocales(texto):
    vocals = "aeiouAEIOU"
    return str(sum(1 for letra in texto if letra in vocals))
    pass
