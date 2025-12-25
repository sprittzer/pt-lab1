from abc import ABC, abstractmethod

class EuropeanSocket:
    def power_on_european(self):
        return "220V power from European socket"

class USASocket:
    def power_on_usa(self):
        return "110V power from USA socket"

class SocketAdapter(ABC):
    @abstractmethod
    def power_on(self):
        pass

class EuropeanAdapter(SocketAdapter):
    def __init__(self):
        self.socket = EuropeanSocket()
    
    def power_on(self):
        return self.socket.power_on_european()

class USAAdapter(SocketAdapter):
    def __init__(self):
        self.socket = USASocket()
    
    def power_on(self):
        return self.socket.power_on_usa()

class Device:
    def __init__(self, adapter: SocketAdapter):
        self.adapter = adapter
    
    def charge(self):
        return f"Device charging with {self.adapter.power_on()}"

if __name__ == "__main__":
    european_adapter = EuropeanAdapter()
    usa_adapter = USAAdapter()
    
    device1 = Device(european_adapter)
    print(device1.charge())
    
    device2 = Device(usa_adapter)
    print(device2.charge())