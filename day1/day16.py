
money_machine = MoneyMachine()
money_machine.report()
menu = Menu()
coffee_maker = CoffeeMaker()
coffee_maker.report()

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
