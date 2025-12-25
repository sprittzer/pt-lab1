from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        return "Телевизор включен"
    
    def turn_off(self):
        return "Телевизор выключен"

class Radio(Device):
    def turn_on(self):
        return "Радио включено"
    
    def turn_off(self):
        return "Радио выключено"

class Remote(ABC):
    def __init__(self, device: Device):
        self.device = device
    
    @abstractmethod
    def power(self):
        pass

class BasicRemote(Remote):
    def power(self):
        return self.device.turn_on()

class AdvancedRemote(Remote):
    def power(self):
        return self.device.turn_on() + " с дополнительными настройками"

if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    basic_tv = BasicRemote(tv)
    advanced_radio = AdvancedRemote(radio)
    
    print(basic_tv.power())
    print(advanced_radio.power())