from abc import ABC, abstractmethod
import time

class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> str:
        pass

class RealDatabase(Database):
    def query(self, sql: str) -> str:
        time.sleep(2)
        return f"Результат запроса: {sql}"

class DatabaseProxy(Database):
    def __init__(self):
        self._real_database = None
        self._cache = {}
    
    def query(self, sql: str) -> str:
        if sql in self._cache:
            print("Прокси: возвращаю результат из кэша")
            return self._cache[sql]
        
        if not self._real_database:
            print("Прокси: создаю реальную базу данных")
            self._real_database = RealDatabase()
        
        print("Прокси: выполняю запрос к базе данных")
        result = self._real_database.query(sql)
        self._cache[sql] = result
        return result

if __name__ == "__main__":
    proxy = DatabaseProxy()
    
    print("Первый запрос (будет долго):")
    print(proxy.query("SELECT * FROM users"))
    
    print("\nПовторный запрос (быстро из кэша):")
    print(proxy.query("SELECT * FROM users"))
    
    print("\nНовый запрос (снова долго):")
    print(proxy.query("SELECT * FROM orders"))