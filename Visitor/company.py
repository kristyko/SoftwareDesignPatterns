from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List


# ========== VISITORS ==========

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
    def visit_stafflist(self, employee: StaffList):
        pass


class SalaryUpgradeVisitor(ABC):
    def __init__(self, percent=5):
        self._percent = percent

    def _raise_salary(self, employee: Employee):
        salary = employee.get_salary()
        return employee.set_salary(salary * (1 + self._percent / 100))

    def visit_manager(self, employee: Manager):
        self._raise_salary(employee)
        print(f"manager's salary raised by {self._percent} per cent")

    def visit_salesperson(self, employee: SalesPerson):
        self._raise_salary(employee)
        print(f"Salesperson's salary raised by {self._percent} per cent")

    def visit_itservice(self, employee: ITService):
        self._raise_salary(employee)
        print(f"IT Service's salary raised by {self._percent} per cent")

    def visit_stafflist(self, employee: Employee):
        print(f"All team's salary is going to be raised by {self._percent} per cent")


class SalaryDowngradeVisitor(ABC):
    def __init__(self, fine: float):
        self._fine = fine

    def _punish_employee(self, employee: Employee):
        salary = employee.get_salary()
        employee.set_salary(salary - self._fine)

    def visit_manager(self, employee: Manager):
        self._punish_employee(employee)
        print(f"Manager's salary is going to be shortened by ${self._fine}")

    def visit_salesperson(self, employee: SalesPerson):
        self._punish_employee(employee)
        print(f"Salesperson's salary is going to be shortened by ${self._fine}")

    def visit_itservice(self, employee: ITService):
        self._punish_employee(employee)
        print(f"IT Service's salary is going to be shortened by ${self._fine}")

    def visit_stafflist(self, employee: Employee):
        print(f"All team's salary is going to be shortened by ${self._fine}")


# ========== STAFF MEMBERS ==========

class Employee(ABC):
    _salary: float

    def get_salary(self):
        return self._salary

    def set_salary(self, salary: float): pass

    @abstractmethod
    def accept(self, visitor: SalaryVisitor):
        pass


class Manager(Employee):
    def __init__(self, salary: float):
        self._salary = salary

    def set_salary(self, salary: float):
        self._salary = salary

    def accept(self, visitor):
        visitor.visit_manager(self)


class SalesPerson(Employee):
    def __init__(self, salary: float):
        self._salary = salary

    def set_salary(self, salary: float):
        self._salary = salary

    def accept(self, visitor):
        visitor.visit_salesperson(self)


class ITService(Employee):
    def __init__(self, salary: float):
        self._salary = salary

    def set_salary(self, salary: float):
        self._salary = salary

    def accept(self, visitor):
        visitor.visit_itservice(self)


class StaffList(Employee):
    def __init__(self, employees: List[Employee] = None):
        if employees is None:
            employees = []
        self._employees = employees

    def add_employee(self, employee: Employee) -> None:
        self._employees.append(employee)

    def get_salary(self) -> float:
        return sum([employee.get_salary() for employee in self._employees])

    def accept(self, visitor: SalaryVisitor):
        visitor.visit_stafflist(self)
        for employee in self._employees:
            employee.accept(visitor)


if __name__ == '__main__':
    staffList = StaffList()

    staffList.add_employee(Manager(60000))
    staffList.add_employee(SalesPerson(50000))
    staffList.add_employee(SalesPerson(40000))

    print(f"Total amount paid to staff: {staffList.get_salary()}")

    it_service = ITService(345363)
    staffList.add_employee(it_service)

    fine_visitor = SalaryDowngradeVisitor(300)
    fine_visitor.visit_itservice(it_service)
    fine_visitor.visit_stafflist(staffList)
    print(f"Total amount paid to staff: {staffList.get_salary()}")

# Total amount paid to staff: 150000
# IT Service's salary is going to be shortened by $300
# All team's salary is going to be shortened by $300
# Total amount paid to staff: 495063
