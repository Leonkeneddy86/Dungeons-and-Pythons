def recolectar_recurso(recursos, recurso_buscado):
    if recurso_buscado in recursos:
        return  f"Has recolectado {recurso_buscado}!"
    return f"{recurso_buscado} no está disponible en la mazmorra."
    pass
