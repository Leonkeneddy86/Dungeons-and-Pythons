def calcular_damage_hechizo(damage_base, multiplicador):
    if multiplicador <1:
        return str(damage_base)
    return str(int(damage_base*multiplicador))
    pass
