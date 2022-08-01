from asyncio.windows_events import NULL
import Pyro4
from server import Persona

if __name__=='__main__':
    uri = input("uri:").strip()

    name = input("Name:").strip()
    
    person = Pyro4.Proxy(uri) # se crea el proxy
    respuesta = Persona(person)
    print (respuesta.get_saludo(name))
    respuesta.shutdown(person)
    person._pyroRelease() # esto es para eliminar el proxy si no esta en uso
    print ('client exiting...')





  





