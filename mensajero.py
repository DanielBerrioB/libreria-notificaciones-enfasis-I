from abc import ABC, abstractmethod

class Mensajero():
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class SMS(Mensajero):
    def enviar(self, mensaje: str):
        return f'Enviando: {mensaje} via: SMS'

class Facebook(Mensajero):
    def enviar(self, mensaje: str):
        return f'Enviando: {mensaje} via: FACEBOOK'

class SMSEmpresarial(Mensajero):
    def enviar(self, mensaje: str):
        return f'Enviando: {mensaje} via: SMS EMPRESARIAL'