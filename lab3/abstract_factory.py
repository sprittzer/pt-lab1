from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Table(ABC):
    @abstractmethod
    def put(self):
        pass

class ModernChair(Chair):
    def sit(self):
        return "Сижу на современном стуле"

class ModernTable(Table):
    def put(self):
        return "Ставлю на современный стол"

class ClassicChair(Chair):
    def sit(self):
        return "Сижу на классическом стуле"

class ClassicTable(Table):
    def put(self):
        return "Ставлю на классический стол"

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        pass

class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    
    def create_table(self):
        return ModernTable()

class ClassicFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()
    
    def create_table(self):
        return ClassicTable()

def create_room(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    
    print(f"Мебель в стиле: {factory.__class__.__name__}")
    print(f"Стул: {chair.sit()}")
    print(f"Стол: {table.put()}")
    print()

if __name__ == "__main__":
    modern = ModernFactory()
    create_room(modern)
    
    classic = ClassicFactory()
    create_room(classic)