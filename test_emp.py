from core import check_valid_name
from fixtures import db


def test_check_valid_name_2(db):
    emp1 = db.get_emp_by_id(1)
    assert check_valid_name.check_name_valid(emp1['name']) is True


def test_check_valid_name_3(db):
    emp2 = db.get_emp_by_id(2)
    assert check_valid_name.check_name_valid(emp2['name']) is False
