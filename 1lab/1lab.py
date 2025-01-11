from abc import ABC, abstractmethod #Импортируем ABC (Abstract Base Class) и abstractmethod из модуля abc для создания абстрактных классов.
import doctest #Импортируем модуль doctest, который позволяет тестировать код, используя примеры в строках документации
class Window(ABC):
    """
    Абстрактный класс, представляющий окно.
    """
    def __init__(self, width: float, height: float, material: str):
        """
        Создание объекта окна.

        :param width: Ширина окна.
        :param height: Высота окна.
        :param material: Материал окна (например, стекло, пластик).

        Пример:
        >>> window = GlassWindow(120, 150, "glass")
        """
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота окна должна быть положительным числом.")
        if not isinstance(material, str) or not material:
            raise ValueError("Материал окна должен быть строкой.")

        self.width = width
        self.height = height
        self.material = material

    @abstractmethod
    def open_window(self) -> None:
        """
        Открыть окно.
        """
        ...

    @abstractmethod
    def close_window(self) -> None:
        """
        Закрыть окно.
        """
        ...


class Gym(ABC):
    """
    Абстрактный класс, представляющий тренажерный зал.
    """
    def __init__(self, name: str, capacity: int, has_pool: bool):
        """
        Создание объекта тренажерного зала.

        :param name: Название зала.
        :param capacity: Вместимость зала (количество людей).
        :param has_pool: Наличие бассейна.

        Пример:
        >>> gym = FitnessGym("StrongFit", 100, True)
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Название зала должно быть строкой.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость зала должна быть положительным числом.")
        if not isinstance(has_pool, bool):
            raise ValueError("Наличие бассейна должно быть булевым значением.")

        self.name = name
        self.capacity = capacity
        self.has_pool = has_pool

    @abstractmethod
    def add_member(self, member_name: str) -> None:
        """
        Добавить нового клиента в зал.

        :param member_name: Имя клиента.
        """
        ...

    @abstractmethod
    def remove_member(self, member_name: str) -> None:
        """
        Удалить клиента из зала.

        :param member_name: Имя клиента.
        """
        ...


class Instagram(ABC):
    """
    Абстрактный класс, представляющий социальную сеть Instagram.
    """

    def __init__(self, username: str, followers: int, following: int):
        """
        Создание объекта профиля Instagram.

        :param username: Имя пользователя.
        :param followers: Количество подписчиков.
        :param following: Количество подписок.

        Пример:
        >>> profile = PersonalInstagram("john_doe", 1500, 300)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Имя пользователя должно быть строкой.")
        if not isinstance(followers, int) or followers < 0:
            raise ValueError("Количество подписчиков должно быть неотрицательным числом.")
        if not isinstance(following, int) or following < 0:
            raise ValueError("Количество подписок должно быть неотрицательным числом.")

        self.username = username
        self.followers = followers
        self.following = following

    @abstractmethod
    def post_photo(self, photo_caption: str) -> None:
        """
        Опубликовать фото.

        :param photo_caption: Подпись к фото.
        """
        ...

    @abstractmethod
    def follow_user(self, username: str) -> None:
        """
        Подписаться на пользователя.

        :param username: Имя пользователя.
        """
        ...
#Проверяем, работают ли примеры из строк документации, с помощью doctest.testmod().
if __name__ == "__main__":
    doctest.testmod()