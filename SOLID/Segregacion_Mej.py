from abc import ABC, abstractmethod


# Interfaces pequeñas y enfocadas
class Switchable(ABC):
    @abstractmethod
    def turn_on(self) -> None: pass
    
    @abstractmethod
    def turn_off(self) -> None: pass


class TemperatureRegulatable(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int) -> None: pass


# Implementaciones concretas
class SmartLight(Switchable):
    def turn_on(self) -> None:
        print("Turning lights ON")
    
    def turn_off(self) -> None:
        print("Turning lights OFF")


class SmartTherm(Switchable, TemperatureRegulatable):
    def turn_on(self) -> None:
        print("Turning temperature ON")
    
    def turn_off(self) -> None:
        print("Turning temperature OFF")
    
    def set_temperature(self, temperature: int) -> None:
        print(f"Setting temperature {temperature}")


# Funciones polimórficas seguras
def power_cycle(device: Switchable) -> None:
    device.turn_off()
    device.turn_on()


def set_safe_temperature(device: TemperatureRegulatable, temp: int) -> None:
    device.set_temperature(temp)


# EJEMPLOS DE USO
smartLight = SmartLight()
power_cycle(smartLight)

smartTherm = SmartTherm()
power_cycle(smartTherm)
set_safe_temperature(smartTherm, 22)