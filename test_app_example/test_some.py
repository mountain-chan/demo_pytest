import json


def login_with_user_admin(test_client):
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
    return access_token


def test_login_with_admin(test_client):
    """

    Args:
        test_client:

    Returns:

    """
    response = test_client.post(
        '/api/v1/auth/login',
        json={"username": "admin", "password": "Admin@1234"}
    )
    json_response = json.loads(response.data.decode())
    data = json_response['data']
    assert json_response['code'] == 200
    assert json_response['status'] is True
    assert data['group'] == 'Admin'
    assert data['username'] == 'admin'


def test_update_profile(test_client, access_token_user_admin):
    """

    Args:
        test_client:
        access_token_user_admin:

    Returns:

    """
    # try to get this user profile
    response = test_client.put(
        '/api/v1/users/profile'.format(),
        headers={'Authorization': 'Bearer {}'.format(access_token_user_admin)},
        json={
            'firstname': 'Mofa1',
            'lastname': 'Admin1'
        }
    )
    json_response = json.loads(response.data.decode())
    data = json_response['data']
    assert json_response['code'] == 200
    assert json_response['status'] is True
    assert data['firstname'] == 'Mofa1'
    assert data['lastname'] == 'Admin1'


def test_get_profile(test_client, access_token_user_admin):
    """
    Args:
        test_client:
        access_token_user_admin:

    Returns:

    """

    # try to get this user profile
    response = test_client.get(
        '/api/v1/users/profile',
        headers={'Authorization': 'Bearer {}'.format(access_token_user_admin)}
    )
    json_response = json.loads(response.data.decode())
    data = json_response['data']
    assert json_response['code'] == 200
    assert json_response['status'] is True
    assert data['group'] == 'Admin'
    assert data['username'] == 'admin'
    assert data['firstname'] == 'Mofa1'
    assert data['lastname'] == 'Admin1'
