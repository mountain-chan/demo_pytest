from core.employee_db import EmployeeBD
import pytest


@pytest.fixture(scope='session')
def db():
    print('-----setUp-----')
    db = EmployeeBD()
    db.connect('data_mock/data.json')
    yield db
    print('-----teardown-----')
    db.close()
