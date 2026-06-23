"""
Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.

Manager має атрибут department.
Developer має атрибут programming_language.

Створіть клас TeamLead, який успадковується від Manager та Developer.
TeamLead повинен мати всі атрибути Manager і Developer,
а також атрибут team_size.

Напишіть тест, який перевіряє наявність атрибутів
з Manager та Developer у класі TeamLead.
"""
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

# Create TeamLead object for testing
team_lead = TeamLead(
    name="Roman",
    salary=10000,
    department="IT",
    programming_language="Python",
    team_size=15
)

assert hasattr(team_lead, "name")
assert hasattr(team_lead, "salary")
assert hasattr(team_lead, "department")
assert hasattr(team_lead, "programming_language")
assert hasattr(team_lead, "team_size")