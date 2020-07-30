import json

import pytest

from app.app import create_app
from app.extensions import db
from app.models import User, SecurityPolicy, Group, PermissionDetail, GroupPermission, Message
from app.settings import TestConfig


@pytest.fixture(scope='module')
def new_user():
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_object=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    # init database
    db.drop_all()
    db.create_all()
    try:
        with open('migrate/default.json') as json_file:
            test_data = json.load(json_file)
    except:
        with open('../migrate/default.json') as json_file:
            test_data = json.load(json_file)

    # insert default security policy
    for item in test_data['security_policy']:
        policy = SecurityPolicy()
        for key in item.keys():
            policy.__setattr__(key, item[key])
        db.session.add(policy)

    # insert default group
    for item in test_data['groups']:
        group = Group()
        for key in item.keys():
            group.__setattr__(key, item[key])
        db.session.add(group)

    # insert test user
    for item in test_data['users']:
        user = User()
        for key in item.keys():
            user.__setattr__(key, item[key])
        db.session.add(user)

    # insert test permissions
    for item in test_data['permissions']:
        instance = PermissionDetail()
        for key in item.keys():
            instance.__setattr__(key, item[key])
        db.session.add(instance)

    # insert test group permissions
    for item in test_data['group_permissions']:
        instance = GroupPermission()
        for key in item.keys():
            instance.__setattr__(key, item[key])
        db.session.add(instance)

    # insert test messages
    for item in test_data['messages']:
        instance = Message()
        for key in item.keys():
            instance.__setattr__(key, item[key])
        db.session.add(instance)

    # Commit the changes for the users
    db.session.commit()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope='module')
def access_token_user_admin(test_client):
    """Login with admin user
    Return:
        access_token: string
    """
    # get access token
    response = test_client.post(
        '/api/v1/auth/login',
        json={"username": "admin", "password": "Admin@1234"}
    )
    json_response = json.loads(response.data.decode())
    data = json_response['data']
    access_token = data['access_token']
    yield access_token
