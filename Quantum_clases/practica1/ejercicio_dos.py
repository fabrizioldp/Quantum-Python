longitud = float(input('Ingrese la longitud del polígono: '))
ancho = float(input('Ingrese el ancho del polígono: '))

def area_o_perimetro (longitud, ancho):
    area = longitud * longitud
    perimetro = longitud * 2 + ancho * 2
    if longitud == ancho:
        print(f'El área del cuadrado es {area}')
    elif longitud != ancho:
        print(f'El perímetro del rectángulo es {perimetro}')


if longitud == ancho:
        area_o_perimetro(longitud, ancho)
elif longitud != ancho:
        area_o_perimetro(longitud, ancho)