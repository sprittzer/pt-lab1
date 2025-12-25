from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def save(self, filename):
        pass


class PDFDocument(Document):
    def render(self):
        return "Рендеринг PDF документа"
    
    def save(self, filename):
        return f"PDF документ сохранен как {filename}.pdf"


class WordDocument(Document):
    def render(self):
        return "Рендеринг Word документа"
    
    
    def save(self, filename):
        return f"Word документ сохранен как {filename}.docx"


class ExcelDocument(Document):
    def render(self):
        return "Рендеринг Excel таблицы"
    
    def save(self, filename):
        return f"Excel таблица сохранена как {filename}.xlsx"


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass
    
    def process_document(self, filename):
        document = self.create_document()
        print(document.render())
        print(document.save(filename))
        return document


class PDFCreator(DocumentCreator):
    def create_document(self):
        return PDFDocument()


class WordCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()


class ExcelCreator(DocumentCreator):
    def create_document(self):
        return ExcelDocument()


if __name__ == "__main__":
    print("Создание pdf документа:")
    pdf_creator = PDFCreator()
    pdf_doc = pdf_creator.process_document("report")
    
    print("\nСоздание word документа:")
    word_creator = WordCreator()
    word_doc = word_creator.process_document("essay")
    
    print("\nСоздание excel документа:")
    excel_creator = ExcelCreator()
    excel_doc = excel_creator.process_document("data")
    
    print(f"\nPDF документ: {type(pdf_doc).__name__}")
    print(f"Word документ: {type(word_doc).__name__}")
    print(f"Excel документ: {type(excel_doc).__name__}")