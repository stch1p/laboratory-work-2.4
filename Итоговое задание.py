class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, users: int):
        """
        Инициализация социальной сети.

        :name: Название социальной сети.
        :users: Количество пользователей в социальной сети.
        """
        self.name = name
        self._users = users

    @property
    def users(self) -> int:
        """Возвращает количество пользователей в социальной сети."""
        return self._users

    @users.setter
    def users(self, number_users: int):

        if not isinstance(number_users, int):
            raise TypeError("Количество пользователей должно быть типа int.")
        if number_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self._users = number_users

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.
        """
        return f"{self.name} - Пользователей: {self.users}"

    def __repr__(self) -> str:
        """
        Возвращает представление социальной сети.
        """
        return f"SocialNetwork(name='{self.name}', users={self.users})"

    def __eq__(self, other: 'SocialNetwork') -> bool:
        """
        Сравнивает текущую социальную сеть с другой по названию.

        """
        return self.name == other.name


class VK(SocialNetwork):
    """Класс, представляющий социальную сеть VK, унаследованный от SocialNetwork."""

    def __init__(self, name: str, users: int, groups: int):
        """
        Инициализация социальной сети VK.

        :name: Название социальной сети.
        :users: Количество пользователей в социальной сети.
        :groups: Количество групп в социальной сети VK.
        """
        super().__init__(name, users)
        self._groups = groups

    @property
    def groups(self) -> int:
        """Возвращает количество групп в социальной сети VK."""
        return self._groups

    @groups.setter
    def groups(self, number_groups: int):
        """
        Устанавливает количество групп в социальной сети VK.
        """
        if not isinstance(number_groups, int):
            raise TypeError("Количество групп должно быть типа int.")
        if number_groups < 0:
            raise ValueError("Количество групп не может быть отрицательным.")
        self._groups = number_groups

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети VK.

        """
        return f"{super().__str__()} - Групп: {self.groups}"

    def __eq__(self, other: 'VK') -> bool:
        """
        Сравнивает текущую социальную сеть VK с другой по названию.

        """
        return super().__eq__(other)


class Facebook(SocialNetwork):
    """Класс, представляющий социальную сеть Facebook, унаследованный от SocialNetwork."""

    def __init__(self, name: str, users: int, pages: int):
        """
        Инициализация социальной сети Facebook.

        :name: Название социальной сети.
        :users: Количество пользователей в социальной сети.
        :pages: Количество страниц в социальной сети Facebook.
        """
        super().__init__(name, users)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в социальной сети Facebook."""
        return self._pages

    @pages.setter
    def pages(self, number_pages: int):
        """
        Устанавливает количество страниц в социальной сети Facebook.

        """
        if not isinstance(number_pages, int):
            raise TypeError("Количество страниц должно быть типа int.")
        if number_pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным.")
        self._pages = number_pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети Facebook.

        """
        return f"{super().__str__()} - Страниц: {self.pages}"

    def __eq__(self, other: 'Facebook') -> bool:
        """
        Сравнивает текущую социальную сеть Facebook с другой по названию.

        """
        return super().__eq__(other)


# Пример использования свойств
vk = VK("VK", 1000000, 50000)
vk.users = 1500000  # Новое значение для пользователей
print(vk.users)  # Вывод: 1500000

facebook = Facebook("Facebook", 2000000, 100000)
facebook.pages = 150000  # Новое значение для страниц
print(facebook.pages)  # Вывод: 150000

# Проверяем равенство социальных сетей
print(vk == facebook)  # Вывод: False



if __name__ == "__main__":
    # Write your solution here
    pass
