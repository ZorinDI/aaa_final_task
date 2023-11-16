from random import randint
import click

from pizza import BasicPizza, Margherita, Pepperoni, Hawaiian

Menu = {'margherita': Margherita, 'pepperoni': Pepperoni, 'hawaiian': Hawaiian}


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery/--pickup', 'deliver_flag', default=False)
@click.option("--size", default="L")
@click.argument('pizza', nargs=1)
def order(pizza: str, deliver_flag: bool, size: str) -> None:
    """Функция для заказа"""
    if pizza.lower() not in Menu:
        print(f'{pizza} не входит в наше меню')
    else:
        pizza = Menu[pizza](size=size)
        name, ingredients = list(pizza.dict().items())[0]
        print(f'Вы заказали - {name} {pizza.emoji}: {"".join(ingredients)} (размер: {pizza.size})')
        bake(pizza)
        delivery(pizza) if deliver_flag else pickup(pizza)


@cli.command()
def menu() -> None:
    """Показывает меню"""
    for name in Menu:
        pizza = Menu[name]()
        type, ingredients = list(pizza.dict().items())[0]
        click.echo(f'- {type} {pizza.emoji}: {"".join(ingredients)}')


def log(text):
    def inner(func):
        def wrapper(pizza: BasicPizza):
            value = func(pizza)
            print(text.replace("{}", f"{randint(0, 10)}"))
            return value

        return wrapper

    return inner


@log('🍍Приготовили за {} с!')
def bake(pizza: BasicPizza) -> None:
    """Пичот пиццу"""
    pass


@log('🛵 Доставили за {} с!')
def delivery(pizza: BasicPizza) -> None:
    """Доставляет пиццу"""
    pass


@log('🍍Забрали за {}с!')
def pickup(pizza: BasicPizza) -> None:
    """Забирает"""
    pass


if __name__ == '__main__':
    cli()
