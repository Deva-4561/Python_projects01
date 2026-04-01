class Employee:
    def get_salary(self):
        return 0

class Manager(Employee):
    def get_salary(self):
        return 8000

class Developer(Employee):
    def get_salary(self):
        return 5000

employees = [Manager(), Developer()]
for emp in employees:
    print("Salary:", emp.get_salary())