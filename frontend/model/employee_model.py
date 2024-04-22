import requests

class EmployeeModel:
    def __init__(self):
        self.base_url = "http://localhost:5001/employees"

    def fetch_all_employees(self):
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print("Error fetching employees:", str(e))
            return None

    def add_employee(self, data):
        try:
            response = requests.post(self.base_url, json=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Error adding employee:", str(e))
            return False

    def update_employee(self, employee_id, data):
        try:
            response = requests.put(f"{self.base_url}/{employee_id}", json=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Error updating employee:", str(e))
            return False

    def delete_employee(self, employee_id):
        try:
            response = requests.delete(f"{self.base_url}/{employee_id}")
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print("Error deleting employee:", str(e))
            return False
