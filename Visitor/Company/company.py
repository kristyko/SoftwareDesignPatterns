from abc import abstractmethod, ABC
from typing import List

from salary_visitor import SalaryVisitor


class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def accept(self, visitor: SalaryVisitor):
        pass


class Manager(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, salary: int):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def accept(self, visitor):
        visitor.visit_manager(self)


class SalesPerson(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, salary: int):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def accept(self, visitor):
        visitor.visit_salesperson(self)


class ITService(Employee):
    def __init__(self, salary: int):
        self._salary = salary

    def set_salary(self, salary: int):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def accept(self, visitor):
        visitor.visit_itservice(self)


class StaffList(Employee):
    def __init__(self, employees: List[Employee] = None):
        if employees is None:
            employees = []
        self._employees = employees

    def add_employee(self, employee: Employee) -> None:
        self._employees.append(employee)

    def get_salary(self) -> int:
        return sum([employee.get_salary() for employee in self._employees])

    def accept(self, visitor: SalaryVisitor):
        for employee in self._employees:
            employee.accept(visitor)


if __name__ == '__main__':
    staffList = StaffList()

    staffList.add_employee(Manager(60000))
    staffList.add_employee(SalesPerson(50000))
    staffList.add_employee(SalesPerson(40000))

    print(f"Total amount paid to staff: {staffList.get_salary()}")
