class Human:
    def __init__(self, name: str, satiety: int = 50, home: 'House' = None):
        self.name = name
        self.satiety = satiety
        self.home = home

    def __str__(self):
        return f"Имя: {self.name}, сытость: {self.satiety}, {self.home or 'дом отсутствует'}"

    def add_house(self, home):
        self.home = home

    def eat(self):
        """ Метод позволяет человеку поесть """
        self.satiety += 25
        self.home.fridge.food -= 5

    def work(self):
        """ Метод позволяет отправить человека на работу """
        self.satiety -= 20
        self.home.bedside_table.money += 40

    def play(self):
        self.satiety -= 10

    def go_for_food(self):
        """ Метод отправляет человека за едой """
        self.home.fridge.food += 30
        self.home.bedside_table.money -= 70

    def life(self, num):
        """ Метод позволяет прожить один день """
        if self.satiety < 20:
            self.eat()
        elif self.home.fridge.food < 10:
            self.go_for_food()
        elif self.home.bedside_table.money < 50:
            self.work()
        elif num == 1:
            self.work()
        elif num == 2:
            self.eat()
        else:
            self.play()


class House:
    def __init__(self, fridge: 'Refrigerator' = None, bedside_table: 'Nightstand' = None):
        self.fridge = fridge
        self.bedside_table = bedside_table

    def add_refrigerator(self, fridge: 'Refrigerator' = None):
        self.fridge = fridge

    def add_nightstand(self, bedside_table: 'Nightstand' = None):
        self.bedside_table = bedside_table

    def __str__(self):
        return f'{self.fridge or 'еды нет'}, {self.bedside_table or 'денег нет'}'


class Refrigerator:
    def __init__(self, food: int = 50):
        self.food = food

    def __str__(self):
        return f'еды в холодильнике: {self.food}'


class Nightstand:
    def __init__(self, money: int = 0):
        self.money = money

    def __str__(self):
        return f'денег в тумбочке: {self.money}'


def init_home():
    """ Инициализация дома """
    home = House()
    fridge = Refrigerator()
    bedside_table = Nightstand()
    home.add_refrigerator(fridge=fridge)
    home.add_nightstand(bedside_table=bedside_table)
    return home


def main():
    import random
    humans = [Human(name='Anton'), Human(name='Anna')]
    home = init_home()
    for human in humans:
        human.add_house(home)
        print(human)

    for day_index in range(1, 366):
        for human in humans:
            num = random.randint(1, 6)
            human.life(num)
        if any([human.satiety < 0 for human in humans]):
            print('Эксперимент не удался')
            break
    else:
        print('Совместимость 100 %')


if __name__ == '__main__':
    main()
