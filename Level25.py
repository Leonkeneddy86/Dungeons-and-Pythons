def encuentro_monstruos(poder_monstruos, poder_heroe):
    for value in poder_monstruos:
        return str(sum(1 for value in poder_monstruos if value > poder_heroe))
    pass
