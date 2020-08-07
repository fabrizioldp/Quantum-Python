 def imprimir_mensaje(opcion):
    print('Hola')
    print('Cómo estás')
    print(f'elegiste la opción {opcion}')
    print('adios')

   opcion = input('ingresa tu opcion')
   if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
       imprimir_mensaje(opcion)