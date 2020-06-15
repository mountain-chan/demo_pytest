import json


class EmployeeBD:

    def __init__(self):
        self.data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.data = json.load(json_file)

    def get_emp_by_id(self, id):
        for emp in self.data['employees']:
            if emp['id'] == id:
                return emp

    def close(self):
        # close connection in here
        pass
