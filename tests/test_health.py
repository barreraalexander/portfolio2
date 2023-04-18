import pytest

def test_getHealth(client):
    res = client.get('/healthcheck')
    print (res)
    assert res.status_code == 200