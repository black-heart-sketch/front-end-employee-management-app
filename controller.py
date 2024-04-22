from model.model import EmployeeModel

class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()

    def get_all_employees(self):
        return self.model.fetch_all_employees()

    def add_employee(self, name, age, doj, email, gender, contact, address):
        self.model.insert_employee(name, age, doj, email, gender, contact, address)

    def update_employee(self, id, name, age, doj, email, gender, contact, address):
        self.model.update_employee(id, name, age, doj, email, gender, contact, address)

    def delete_employee(self, id):
        self.model.delete_employee(id)
