class BasicPizza:
    """Main Class, other classes will be inhereted from this class"""

    def __init__(self, name='Pizza', size='L', ingredients=None):
        if ingredients is None:
            self._ingredients = ['']
        else:
            self._ingredients = ingredients
        self.name = name
        self.size = size

    @property
    def ingredients(self):
        """Comma separated ingredients"""
        return ", ".join(self._ingredients)

    def dict(self):
        """Dict function"""
        return {self.name: self.ingredients}

    def __str__(self):
        """Return stroke like in menu"""
        return f'Pizza: {self.name}, size: {self.size}'

    def __eq__(self, other):
        """Check the equality"""
        return self.dict() == other.dict() and self.size == other.size


class Margherita(BasicPizza):
    """Making pizza Margherita"""
    emoji = "🧀"

    def __init__(self, size='L'):
        ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(name='Margherita', size=size, ingredients=ingredients)


class Pepperoni(BasicPizza):
    """Making pizza Pepperoni"""
    emoji = "🍕"

    def __init__(self, size='L'):
        ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(name='Pepperoni', size=size, ingredients=ingredients)


class Hawaiian(BasicPizza):
    """Making Hawaiian pizza"""
    emoji = "🍍"

    def __init__(self, size='L'):
        ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        super().__init__(name='Hawaiian', size=size, ingredients=ingredients)


if __name__ == '__main__':
    pass
