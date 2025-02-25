def actualizar_inventario(inventario, objeto, capacidad, accion):
    if accion == "agregar" and len(inventario) < capacidad:
        inventario.append(objeto)
    elif accion == "eliminar" and objeto in inventario:
        inventario.remove(objeto)
    return str(inventario)
    pass
