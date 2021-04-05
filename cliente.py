from notificador import Notificador
from aplicacion import Aplicacion

msg_1 = {
    "facebook": "Hola mundo",
    "sms": "Hola mundo",
    "smsempresarial": "Hola mundo"
}

msg_2 = {
    "facebook": "Mensaje 2",
    "sms": "Mensaje 2",
}

notifier_1 = Notificador(msg_1)
notifier_2 = Notificador(msg_2)

app = Aplicacion()

app.notificador(notifier_1)
app.notificador(notifier_2)