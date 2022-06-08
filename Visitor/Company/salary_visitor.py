from abc import ABC, abstractmethod

from company import Manager, StaffList, ITService, SalesPerson, Employee


class SalaryVisitor(ABC):
    @abstractmethod
    def visit_manager(self, employee: Manager):
        pass

    @abstractmethod
    def visit_salesperson(self, employee: SalesPerson):
        pass

    @abstractmethod
    def visit_itservice(self, employee: ITService):
        pass

    @abstractmethod
    def visit_stufflist(self, employee: StaffList):
        pass


class SalaryUpgradeVisitor(ABC):
    def __init__(self, percent=5):
        self._percent = percent

    def visit_manager(self, employee: Manager):
        salary = employee.get_salary()
        return employee.set_salary(salary * (1 + self._percent / 100))

    def visit_salesperson(self, employee: SalesPerson):
        salary = employee.get_salary()
        return employee.set_salary(salary * (1 + self._percent / 100))

    def visit_itservice(self, employee: ITService):
        salary = employee.get_salary()
        return employee.set_salary(salary * (1 + self._percent / 100))

    def visit_stufflist(self, employee: StaffList):
        for 


class SalaryDowngradeVisitor(ABC):
    def visit_manager(self, employee: Manager):
        salary = employee.get_salary()
        employee.set_salary()

    def visit_salesperson(self, employee: SalesPerson):
        pass

    def visit_itservice(self, employee: ITService):
        pass

    def visit_stufflist(self, employee: StaffList):
        pass
