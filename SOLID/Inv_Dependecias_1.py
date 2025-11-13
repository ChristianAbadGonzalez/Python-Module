# EJEMPLO DE APLICACION CON NOTIFICACION
from abc import ABC, abstractmethod


# Abstracción para el servicio de notificación (interfaz)
# Módulo de alto nivel depende de esta abstracción, no de implementaciones concretas (DIP).
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None: pass # Contrato: toda implementación debe poder enviar un mensaje.


# Implementación concreta para notificación por correo electrónico
# Clase de bajo nivel (detalles concretos)
class EmailNotificador(Notificador):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando email: {mensaje}")


# Implementación concreta para notificación por SMS
# Clase de bajo nivel (detalles concretos)
class SmsNotificador(Notificador):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando sms: {mensaje}")


# Módulo de alto nivel que maneja la lógica de negocio
# Depende de la abstracción Notificador, no de clases concretas (DIP).
class App:
    def __init__(self, notificador: Notificador) -> None:  # Inversión de Dependencias
        # Inyección de dependencias por constructor
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str) -> None:
        # Delegamos en la abstracción: polimorfismo
        self.notificador.enviar(mensaje)
        print("Notificación enviada correctamente")


# EJEMPLOS DE USO
email_notificador = EmailNotificador()
app_con_email = App(email_notificador)  # Inyección de dependencias (constructor)
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electrónico")

sms_notificador = SmsNotificador()
app_con_sms = App(sms_notificador)
app_con_sms.enviar_notificacion("Este es un mensaje de prueba de SMS")

# Reutilización: puedes construir otra App con el notificador que quieras
email_notificador = EmailNotificador()
app_con_email = App(email_notificador)
app_con_email.enviar_notificacion("Este es un mensaje de prueba de correo electrónico")