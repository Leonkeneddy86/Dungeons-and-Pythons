
def invocar_jefe(dificultad, jugadores):
    if dificultad >4 and len(jugadores) > 2:
        return str({'jefe': 'Dragón de Fuego', 'recompensa': 'Espada Legendaria'})
    else:
        return "No hay suficientes jugadores o la dificultad es demasiado baja"
    pass
