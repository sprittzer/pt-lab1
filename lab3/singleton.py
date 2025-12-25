class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = []
            print("Singleton инициализирован")
    
    def add_data(self, item):
        self.data.append(item)
    
    def get_data(self):
        return self.data


if __name__ == "__main__":
    s1 = Singleton()
    s1.add_data("Данные 1")
    
    s2 = Singleton()
    s2.add_data("Данные 2")
    
    print(f"s1 is s2: {s1 is s2}")
    print(f"Данные в s1: {s1.get_data()}")
    print(f"Данные в s2: {s2.get_data()}")