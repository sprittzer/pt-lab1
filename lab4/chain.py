from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class TechnicalSupportHandler(Handler):
    def handle(self, request):
        if request == "technical":
            return "Техподдержка: решаем техническую проблему"
        else:
            return super().handle(request)

class BillingSupportHandler(Handler):
    def handle(self, request):
        if request == "billing":
            return "Биллинг: решаем вопросы оплаты"
        else:
            return super().handle(request)

class GeneralSupportHandler(Handler):
    def handle(self, request):
        if request == "general":
            return "Общая поддержка: отвечаем на общие вопросы"
        else:
            return super().handle(request)

class DefaultHandler(Handler):
    def handle(self, request):
        return f"Не могу обработать запрос: {request}"

if __name__ == "__main__":
    technical = TechnicalSupportHandler()
    billing = BillingSupportHandler()
    general = GeneralSupportHandler()
    default = DefaultHandler()

    technical.set_next(billing).set_next(general).set_next(default)

    requests = ["technical", "billing", "general", "unknown"]

    for req in requests:
        print(f"Запрос: {req}")
        result = technical.handle(req)
        print(f"Ответ: {result}\n")