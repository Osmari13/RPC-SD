import Pyro4
Pyro4.config.COMMTIMEOUT=1.0 #se establece un tiempo de espera para el daemon
@Pyro4.expose #una forma segura de manejar las clases que se accenden de forma remota

class Persona(object): #en la clase persona se especifica lo que quiere que haga el servidor
    def __init__(self, daemon):
        self.daemon = daemon
        self.running = True
    def get_saludo(self,name):
        return "Hola, {0}".format(name)
    @Pyro4.oneway #para hacer llamadas unidireccionales
    def shutdown(self):
        print('apagando...')
        self.running=False
if __name__=='__main__':
    daemon = Pyro4.Daemon() #se crea el objeto remoto
    person = Persona(daemon)
    uri = daemon.register(person) # se registra el objeto remoto que nos retornara una identificacion
    def checkshutdown():
        return person.running
    print ("Hola el servidor esta activo")
    print (uri)
    daemon.requestLoop(loopCondition=checkshutdown) # se esperan llamadas y revisa si no se esta operando en el servidor
    daemon.close()#daemon cerrado
  

