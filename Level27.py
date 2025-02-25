def organizar_botin(objetos):
    botin = {}
    for objeto in objetos:
        botin[objeto] = botin.get(objeto, 0) + 1
    return str(botin)
    pass
