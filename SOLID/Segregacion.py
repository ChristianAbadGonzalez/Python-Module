from abc import ABC, abstractmethod

# Interfaz para dispositivos con capacidad de encendido/apagado
class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        """Enciende el dispositivo."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """Apaga el dispositivo."""
        pass


# Interfaz para dispositivos que permiten regular la temperatura
class ITemperatureRegulatable(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int) -> None:
        """Ajusta la temperatura del dispositivo."""
        pass


# Dispositivo inteligente: Luz - Implementa solo la interfaz de encendido/apagado (SRP + ISP)
class SmartLight(ISwitchable):
    def turn_off(self) -> None:
        print("Turning light OFF")

    def turn_on(self) -> None:
        print("Turning light ON")


# Dispositivo inteligente: Termostato - Implementa encendido/apagado + regulación de temperatura
class SmartTemperature(ISwitchable, ITemperatureRegulatable):
    def turn_off(self) -> None:
        print("Turning Temp. OFF")

    def turn_on(self) -> None:
        print("Turning Temp. ON")

    def set_temperature(self, temperature: int) -> None:
        print(f"Setting temperature {temperature}")


# EJEMPLOS DE USO
smartLight = SmartLight()
smartLight.turn_off()
smartLight.turn_on()

smartTherm = SmartTemperature()
smartTherm.turn_off()
smartTherm.turn_on()
smartTherm.set_temperature(10)