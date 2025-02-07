class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self):
        """
        Свойство для получения названия книги. Изменение запрещено.
        """
        return self._name

    def author(self):
        """
        Свойство для получения автора книги. Изменение запрещено.
        """
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление книги для пользователей.
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает строковое представление книги для разработчиков.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    """
    Класс бумажной книги.
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для проверки

    def pages(self):
        """
        Свойство для получения количества страниц.
        """
        return self._pages

    def pages(self, value):
        """
        Проверка значения количества страниц.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        """
        Возвращает строковое представление бумажной книги.
        """
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}"


class AudioBook:
    """
    Класс аудиокниги.
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для проверки

    def duration(self):
        """
        Свойство для получения продолжительности книги.
        """
        return self._duration

    def duration(self, value):
        """
        Проверка значения продолжительности книги.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        """
        Возвращает строковое представление аудиокниги.
        """
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration:.2f} часов"
