from dataclasses import dataclass

from domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str
    
    @property
    def message(self):
        return f'Слишком длинный текст: "{self.text[:255]}..."'
    
@dataclass(eq=False)
class EmptyTextError(ApplicationException):
    
    @property
    def message(self):
        return f'Пустой текст, пожалуйста введите значение'