from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmando)
    assert response.json() == {'message': 'Olar Mundo'}  # Assert (Afirmando)


def test_read_root_deve_retornar_html(client):
    response = client.get('/html')  # Act (ação)

    html_esperado = """
        <html>
        <head>
            <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
        </html>"""

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmando)
    assert response.text == html_esperado  # Assert (Afirmando)


def teste_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Validar status code correto
    assert response.status_code == HTTPStatus.CREATED

    # Validar User Public
    assert response.json() == {
        'username': 'testeusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    # Validar status code correto
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testeusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testeusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User Deleted'}
