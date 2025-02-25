def prueba_elemental(elementos_disponibles, combinacion_requerida):
    for element in combinacion_requerida:
        if combinacion_requerida.count(element) > elementos_disponibles.count(element):
            return "False"
    return "True"

