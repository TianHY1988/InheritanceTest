'''
Employee is the base class for all employee types. 
It is constructed with an id and a name. What you 
are saying is that every Employee must have an id 
assigned as well as a name.
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass
