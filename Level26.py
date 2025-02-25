def generar_nombre_monstruo(prefijos, sufijos, titulos):
    nombres = []

    for prefijo in prefijos:
        for sufijo in sufijos:
            nombres.append(f"{prefijo} {sufijo}")

    if titulos:
        nombres_con_titulo = []
        for titulo in titulos:
            for nombre in nombres:
                nombres_con_titulo.append(f"{titulo} {nombre}")
        return str(nombres_con_titulo)

    return str(nombres)
