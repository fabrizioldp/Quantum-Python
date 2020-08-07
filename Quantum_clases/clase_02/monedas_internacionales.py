mensaje = '''
Hola, este es un conversor de monedas.
Seleccione una de estas tres opciones:
1=soles a dolares
2=euros a dolares
3=pesos colombianos a dolares
'''
print(mensaje)
opcion =int(input('Ingrese la opción'))
if opcion == 1:
    tipo_de_cambio = 0.28
    monto_soles = input('Ingrese su monto en soles')
    monto_soles = float(monto_soles)
    monto_dolares = round(monto_soles * tipo_de_cambio, 2)
    print(f'El monto en dolares es: ' {monto_dolares})
elif opcion == 2:
    tipo_de_cambio = 1.19
    monto_euros = input('Ingrese su monto en euros')
    monto_euros = float(monto_euros)
    monto_dolares = round(monto_euros * tipo_de_cambio, 2)
    print(f'El monto en dolares es:' {monto_dolares})
elif opcion == 3:
    tipo_de_cambio = 0.00027
    monto_colombia = input('Ingrese su monto en pesos colombianos')
    monto_colombia = float(monto_colombia)
    monto_dolares = round(monto_colombia * tipo_de_cambio, 2)
    print(f'El monto en dolares es:' {monto_dolares})