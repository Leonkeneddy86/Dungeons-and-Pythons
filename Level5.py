def calcular_vida(vida, damage):
    if (vida - damage < 0):
        return "0"
    return (vida - damage)