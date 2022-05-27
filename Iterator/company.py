from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List


class Employee:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Employee: {self._name}"


class StaffList(Iterable):
    def __init__(self, staff: List[Employee]):
        self._staff = staff

    @property
    def staff(self):
        return self._staff

    def add_employee(self, employee: Employee):
        self._staff.append(employee)

    def __iter__(self):
        return StaffListIterator(self)


class StaffListIterator(Iterator):
    def __init__(self, staff_list: StaffList):
        self._staff_list = staff_list
        self._index = 0

    def __next__(self):
        try:
            value = self._staff_list.staff[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration()

        return value