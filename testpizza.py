from pizza import BasicPizza, Margherita, Pepperoni, Hawaiian


def test_dict1():
    ingredients = ['mozzarella', 'tomatoes', 'nails']
    pizza = BasicPizza(size='L', ingredients=ingredients)
    assert pizza.dict() == {'Pizza': ", ".join(ingredients)}


def test_basic_size():
    pizza = BasicPizza()
    assert pizza.size == 'L'


def test_dict2():
    pizza = Margherita()
    assert pizza.dict() == {'Margherita': 'tomato sauce, mozzarella, tomatoes'}


def test_dict3():
    pizza = Pepperoni()
    assert pizza.dict() == {'Pepperoni': 'tomato sauce, mozzarella, pepperoni'}


def test_dict4():
    pizza = Hawaiian()
    assert pizza.dict() == {'Hawaiian': 'tomato sauce, mozzarella, chicken, pineapples'}


def test_equality():
    assert Margherita(size='XL') == Margherita(size='XL')


def test_unequality1():
    assert Margherita(size='XL') != Margherita(size='L')


def test_unequality2():
    assert Margherita(size='XL') != Pepperoni(size='XL')


def test_str():
    pizza1 = Margherita()
    pizza2 = Hawaiian()
    assert str(pizza1) == 'Pizza: Margherita, size: L' and str(pizza2) == 'Pizza: Hawaiian, size: L'
