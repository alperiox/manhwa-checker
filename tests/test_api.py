import requests

import pytest

from app import app as api

@pytest.fixture(scope='module')
def app():
    api.config.update({
        "TESTING": True,
    })

    yield api


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_fetch_asura(client):
    # it raises an error:
    # RuntimeError: Event loop is closed
    # but it is being ignored by pytest.
    # I guess asyncio's event loop is forcibly being closed by pytest after
    # the test is done. Since asyncio could not clear up, it raises an error
    # but of course, this is just a simply hypothesis
    r = client.post("/fetch/asura", json={"url":"https://asura.gg/manga/solo-leveling/"})
    expected = {'status': 'Completed', 'latest_chapter': 179, 
     'title': 'Chapter 179',
     'last_updated': 'December 29, 2021', 
     'url': 'https://asura.gg/solo-leveling-chapter-179-end/', 'slug': 'solo-leveling'}
    returned = r.json['results'][0]
    print("Result:", returned)

    assert returned == expected