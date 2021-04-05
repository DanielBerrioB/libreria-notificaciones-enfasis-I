from abc import abstractmethod
from mensajero import Facebook, SMS, SMSEmpresarial

class Notificador:
    def __init__(self, listaMensaje: dict):
        self.listaMensaje = listaMensaje
    
    def enviarTodo(self):
        for key in self.listaMensaje:
            if key.lower() == 'facebook':
                print(Facebook().enviar(self.listaMensaje[key]))
            elif key.lower() == 'sms':
                print(SMS().enviar(self.listaMensaje[key]))
            elif key.lower() == 'smsempresarial':
                print(SMSEmpresarial().enviar(self.listaMensaje[key]))
            else:
                print('Error, intenta de nuevo')