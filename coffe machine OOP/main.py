from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine= MoneyMachine()
coffee_maker= CoffeeMaker()
menu=Menu()



is_on=True

while is_on:
    option= menu.get_items()
    choice= input(f"What do you want to drink? ({option})")
    if choice == "off":
        is_on= False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        recources_ok = coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)
        if recources_ok and payment:
            coffee_maker.make_coffee(drink)






