velocidad = float(input('Ingrese la velocidad que recorre el objeto en kilómetros por hora: '))

def conversion_velocidad (kilometros):
    nueva_velocidad = round(velocidad * 100000, 0)
    print(f'La velocidad recorrida equivale a {nueva_velocidad} cm por segundo.')
  

if velocidad != 0:
    conversion_velocidad(velocidad)
else:
    print('ingrese un número')