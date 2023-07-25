import pytest
from flask import json
from main import app

@pytest.fixture
def client():
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client

def test_hello(client):
  sets = []
  for _ in range(3):
    response = client.get('/hello?name=your_name')
    data = json.loads(response.data)
    lucky_numbers_str = data['output'].split(': ')[-1]
    lucky_numbers = set(int(n) for n in lucky_numbers_str.split(', '))
    assert len(lucky_numbers) == 7
    sets.append(lucky_numbers)
  assert len(set(frozenset(s) for s in sets)) == 3
