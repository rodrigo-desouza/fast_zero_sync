from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmando)
    assert response.json() == {'message': 'Olar Mundo'}  # Assert (Afirmando)


def test_read_root_deve_retornar_html():
    client = TestClient(app)  # Arrange (organização)

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
