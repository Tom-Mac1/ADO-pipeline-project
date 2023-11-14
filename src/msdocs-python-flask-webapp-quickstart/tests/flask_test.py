import os
import tempfile
import pytest
from ..app import app

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()

    #app = create_app({
        #'TESTING': True,
        #'DATABASE': db_path,
    #})
    # app = app.run()

    with app.run() as client:
        with app.app_context():
            pass
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_index(client):
    response = client.get('/')
    assert b'Request for index page received' in response.data

def test_favicon(client):
    response = client.get('/favicon.ico')
    assert response.mimetype == 'image/vnd.microsoft.icon'

def test_hello(client):
    response = client.post('/hello', data={'name': 'John'})
    assert b'Request for hello page received with name=John' in response.data

def test_hello_no_name(client):
    response = client.post('/hello')
    assert b'Request for hello page received with no name or blank name -- redirecting' in response.data