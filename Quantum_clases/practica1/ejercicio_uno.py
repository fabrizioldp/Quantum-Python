def hello(n):
    mensaje = f'Hola, {n}'
    print(mensaje)
    
nombre = input('Hola. Ingresa tu nombre, por favor: ')
caracteres_nombre = len(nombre)
if caracteres_nombre == 0:
    print('Hola, mundo.')
else:
    hello(nombre)
