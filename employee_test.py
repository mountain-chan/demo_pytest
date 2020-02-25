from core import check_valid_name
from tests.fixtures import db


def test_first_emp_data(db):
    emp = db.get_emp_by_id(1)
    assert emp['id'] == 1
    assert emp['name'] == 'Chan'
    assert emp['salary'] == 100


def test_second_emp_data(db):
    emp = db.get_emp_by_id(2)
    assert emp['id'] == 2
    assert emp['name'] == 'Chan111'
    assert emp['salary'] == 200


def test_check_valid_name(db):
    emp1 = db.get_emp_by_id(1)
    emp2 = db.get_emp_by_id(2)
    assert check_valid_name.check_name_valid(emp1['name']) is True
    assert check_valid_name.check_name_valid(emp2['name']) is False
