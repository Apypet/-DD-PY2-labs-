class Cosmetics:
    """
    Базовый класс для косметики.
    """

    def __init__(self, name: str, brand: str) -> None:
        self.name = name
        self.brand = brand

    def apply(self) -> str:
        """
        Базовый метод для применения косметики.
        """
        return f"Применяю {self.name} от {self.brand}."

    def __str__(self) -> str:
        return f"Косметика: {self.name}, Бренд: {self.brand}"

    def __repr__(self) -> str:
        return f"Cosmetics(name={self.name}, brand={self.brand})"


class Primer(Cosmetics):
    """
    Класс для праймера, наследуется от Cosmetics.
    """

    def __init__(self, name: str, brand: str, base: str) -> None:
        super().__init__(name, brand)  # Вызов конструктора базового класса
        self.base = base  # Добавление нового атрибута

    def apply(self) -> str:
        """
        Переопределение метода apply.
        Праймер наносится перед макияжем, поэтому логика изменена.
        """
        return f"Наношу {self.name} с {self.base} базой от {self.brand} перед макияжем."

    def __str__(self) -> str:
        return f"Праймер: {self.name}, Бренд: {self.brand}, База: {self.base}"


class Powder(Cosmetics):
    """
    Класс для пудры, наследуется от Cosmetics.
    """

    def set_makeup(self) -> str:
        """
        Новый метод, специфичный для пудры.
        """
        return f"Закрепляю макияж пудрой {self.name} от {self.brand}."


class Clothing:
    """
    Базовый класс для одежды.
    """

    def __init__(self, name: str, size: str) -> None:
        self.name = name
        self.size = size

    def wear(self) -> str:
        """
        Метод для надевания одежды.
        """
        return f"Надеваю {self.name} размера {self.size}."

    def __str__(self) -> str:
        return f"Одежда: {self.name}, Размер: {self.size}"

    def __repr__(self) -> str:
        return f"Clothing(name={self.name}, size={self.size})"


class Skirt(Clothing):
    """
    Класс для юбки, наследуется от Clothing.
    """

    def __init__(self, name: str, size: str, length: str) -> None:
        super().__init__(name, size)
        self.length = length  # Добавление нового атрибута

    def __repr__(self) -> str:
        return f"Skirt(name={self.name}, size={self.size}, length={self.length})"


class Blouse(Clothing):
    """
    Класс для блузки, наследуется от Clothing.
    """

    def iron(self) -> str:
        """
        Новый метод, специфичный для блузки.
        """
        return f"Глажу блузку {self.name} размера {self.size}."


if __name__ == "__main__":
    # Пример использования классов
    primer = Primer("Матирующий праймер", "L'Oreal", "водная")
    print(primer.apply())  # Наношу Матирующий праймер с водная базой от L'Oreal перед макияжем.
    print(primer)  # Праймер: Матирующий праймер, Бренд: L'Oreal, База: водная

    powder = Powder("Минеральная пудра", "Maybelline")
    print(powder.set_makeup())  # Закрепляю макияж пудрой Минеральная пудра от Maybelline.

    skirt = Skirt("Юбка-карандаш", "M", "до колен")
    print(skirt)  # Одежда: Юбка-карандаш, Размер: M
    print(repr(skirt))  # Skirt(name=Юбка-карандаш, size=M, length=до колен)

    blouse = Blouse("Блузка с рюшами", "S")
    print(blouse.iron())  # Глажу блузку Блузка с рюшами размера S.
