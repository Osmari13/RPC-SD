from xmlrpc.server import SimpleXMLRPCServer

class RPC:
    methods_RPC = ['isValid','get'] #se declaran los metodos que va usar el servidor 

    selection={'1':'1','2':'2','3':'3','4':'4'} #se almacena la seleccion dentro del servidor

    def __init__(self, direccion, port): 
        #indica en que direccion y en que puerto se alojara el servidor
        self.server= SimpleXMLRPCServer((direccion, port), allow_none=True)

        for methods in self.methods_RPC: #indica que los metodos declarados son parte del servidor
            self.server.register_function(getattr(self,methods)) # se registran los metodos
    
    def isValid(self, selec): # Es para el reconocimiento del operador
        return selec in self.selection
    
    def get(self, selec): # es el proceso de la operacion que corresponde a la seleccion
        if selec == self.selection['1']:
         producto = ['Leche', 'Queso', 'Yogurt', 'Matequilla', 'Crema de Leche']
        elif selec == self.selection['2']:
          producto = ['Chorizo', 'Jamon', 'Salami', 'Pate', 'Salchicha']
        elif selec == self.selection['3']:
          producto = ['Cebolla', 'Ajo', 'Espinaca', 'Zanahoria', 'Alcachofa']
        elif selec == self.selection['4']:
          producto = ['Cheetos', 'Doritos', 'CheeseTris', 'Lays', 'Natuchips']
        else: 
            return 'Seleccion invalida'
        return producto
    
    def run(self): # es para indicar que el server a iniciado
        self.server.serve_forever() 
        print ("Servidor Activado")

if __name__  == '__main__': 
    rpc = RPC('', 8000) # indica que se ejecute en el host actual y se le asigna un puerto a rpc
    print('Iniciando consultas')
    rpc.run()


        