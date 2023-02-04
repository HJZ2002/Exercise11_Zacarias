class Employee:
    def __init__(self, name, wage):
        self._name = name
        self._salary = wage

    def __repr__(self):
        return self._name + " has a salary of " + str(self._salary) + ".00"


class Manager(Employee):
    def __init__(self, name, wage, department):
        super().__init__(name, wage)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of " + str(
            self._salary) + ".00 and manages the " + self._department + " department"


class Executive(Manager):
    def __init__(self, name, wage, department):
        super().__init__(name, wage, department)

    def __repr__(self):
        return self._name + " has a salary of " + str(
            self._salary) + ".00 and is the executive for the " + self._department + " department"