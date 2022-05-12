from SoftwareDesignPatterns.Composite.post_refactor.company import Manager, Salesperson, SalesTeam


def pay_expenses(working_unit, amount):
    print("Expenses have been requested")
    working_unit.pay_expenses(amount)
    print("Expenses have been paid\n")


if __name__ == '__main__':
    jane = Manager("Jane")
    bob = Salesperson("Bob", jane)
    sue = Salesperson("Sue", jane)

    team = SalesTeam()
    team.add_manager(jane)
    team.add_salesperson(bob)
    team.add_salesperson(sue)

    pay_expenses(jane, 100)
    pay_expenses(bob, 300)
    pay_expenses(team, 200)
