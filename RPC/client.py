import msvcrt
from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:8000", allow_none=True)  # se indica la direccion y el puerto del servidor

while True: # bucle para realizar las consultas
    print('') #menu de opciones
    print('Consultas de Producto')
    print('1. Lacteos')
    print('2. Charcuteria')
    print('3. Hortalizas')
    print('4. Snacks')

    product = input("Selecciones el numero correspondiente al producto: ")

    if proxy.isValid(product): #verifica si la opcion ingresada corresponde a las opciones que estan dentro del servidor
        print("Realizando consulta...")
        print (proxy.get(product)) #muestra la respuesta del servidor
    else:
        print ("Consulta no realizada")

    print ('')
    print ('Presione x para salir...')
    print('Presione cualquier tecla para continuar')

    key = msvcrt.getwch()

    if key == 'x':
        exit()

        