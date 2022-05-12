from SoftwareDesignPatterns.Composite.pre_refactor.manager import Manager
from SoftwareDesignPatterns.Composite.pre_refactor.sales_team import SalesTeam
from SoftwareDesignPatterns.Composite.pre_refactor.salesperson import Salesperson


def pay_manager(manager, amount):
    print("Expenses have been requested")
    manager.pay_expenses(amount)
    print("Expenses have been paid\n")


def pay_salesperson(salesperson, amount):
    print("Expenses have been requested")
    salesperson.pay_expenses(amount)
    print("Expenses have been paid\n")


def pay_team(team, amount):
    print("Expenses have been requested")
    team.pay_expenses(amount)
    print("Expenses have been paid\n")


if __name__ == '__main__':
    jane = Manager("Jane")
    bob = Salesperson("Bob", jane)
    sue = Salesperson("Sue", jane)

    team = SalesTeam()
    team.add_manager(jane)
    team.add_salesperson(bob)
    team.add_salesperson(sue)

    pay_manager(jane, 100)
    pay_salesperson(bob, 300)
    pay_team(team, 200)
