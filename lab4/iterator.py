from collections.abc import Iterator, Iterable

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f'"{self.title}" - {self.author}'

class BookIterator(Iterator):
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            return value
        except IndexError:
            raise StopIteration()

class BookCollection(Iterable):
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def __iter__(self):
        return BookIterator(self._books)
    
    def reverse_iterator(self):
        return BookIterator(self._books, reverse=True)
    
    def get_books(self):
        return self._books

if __name__ == "__main__":
    library = BookCollection()
    library.add_book(Book("Преступление и наказание", "Ф. Достоевский"))
    library.add_book(Book("Война и мир", "Л. Толстой"))
    library.add_book(Book("Мастер и Маргарита", "М. Булгаков"))
    library.add_book(Book("1984", "Дж. Оруэлл"))
    
    print("Прямой порядок:")
    for book in library:
        print(f"  {book}")
    
    print("\nОбратный порядок:")
    for book in library.reverse_iterator():
        print(f"  {book}")
    
    print("\nДоступ по индексу:")
    books = library.get_books()
    print(f"  Первая книга: {books[0]}")
    print(f"  Последняя книга: {books[-1]}")