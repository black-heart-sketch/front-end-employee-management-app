class EmployeeController:
    def __init__(self, model):
        self.model = model

    def fetch_all_employees(self):
        return self.model.fetch_all_employees()

    def add_employee(self, data):
        return self.model.add_employee(data)

    def update_employee(self, employee_id, data):
        return self.model.update_employee(employee_id, data)

    def delete_employee(self, employee_id):
        return self.model.delete_employee(employee_id)
