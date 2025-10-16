from dataclasses import dataclass
from typing import Iterator


@dataclass
class Employee:
    id: int
    name: str

class EmployeeRepository:
    def __init__(self, employees: list[Employee] = None):
        self.employees = employees.copy() if employees else []
    def __iter__(self) -> Iterator[Employee]:
        return iter(self.employees)


repo = EmployeeRepository([Employee(1, "John"), Employee(2, "Jane")])

for employee in repo:
    print(employee)