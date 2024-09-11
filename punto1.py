def generar_serie():
    serie = [5, 8]
    
    while True:
        siguiente_numero = serie[-1] + serie[-2]
        if siguiente_numero == 13:
            siguiente_numero += serie[-1]  # Para saltar el número 13
        if siguiente_numero >= 100:  # Finalizar si se alcanza o supera el número 100
            break
        serie.append(siguiente_numero)
    
    return serie

# Generar la serie y mostrar el resultado
resultado = generar_serie()
print(resultado)
