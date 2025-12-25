from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass


class BubbleSort(SortStrategy):    
    def sort(self, data: List) -> List:
        print("Используется пузырьковая сортировка")
        arr = data.copy()
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


class QuickSort(SortStrategy):
    def sort(self, data: List) -> List:
        print("Используется быстрая сортировка")
        return self._quick_sort(data.copy())
    
    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self._quick_sort(left) + middle + self._quick_sort(right)


class InsertionSort(SortStrategy):
    def sort(self, data: List) -> List:
        print("Используется сортировка вставками")
        arr = data.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


class DataProcessor:
    def __init__(self, data: List):
        self.data = data
        self.sort_strategy = None
    
    def set_sort_strategy(self, strategy: SortStrategy):
        self.sort_strategy = strategy
    
    def process(self) -> List:
        if not self.sort_strategy:
            print("Стратегия сортировки не выбрана")
            return self.data
        
        return self.sort_strategy.sort(self.data)


if __name__ == "__main__":
    print("система сортировки данных")
    
    numbers = [64, 34, 25, 12, 22, 11, 90, 5, 77, 43]
    print(f"Исходный массив: {numbers}")
    
    processor = DataProcessor(numbers)
    
    bubble_sort = BubbleSort()
    quick_sort = QuickSort()
    insertion_sort = InsertionSort()
    
    print("\n1. Пузырьковая сортировка:")
    processor.set_sort_strategy(bubble_sort)
    sorted_data = processor.process()
    print(f"Результат: {sorted_data}")
    
    print("\n2. Быстрая сортировка:")
    processor.set_sort_strategy(quick_sort)
    sorted_data = processor.process()
    print(f"Результат: {sorted_data}")
    
    print("\n3. Сортировка вставками:")
    processor.set_sort_strategy(insertion_sort)
    sorted_data = processor.process()
    print(f"Результат: {sorted_data}")