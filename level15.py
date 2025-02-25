def calcular_damage_final(damages, resistencia):
    totalDamage = sum(damages) * (1 - resistencia)
    return str(int(totalDamage))
    pass
