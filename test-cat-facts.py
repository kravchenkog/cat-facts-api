import requests

BASE_URL = "https://cat-fact.herokuapp.com"

def test_get_random_cat_fact():
    response = requests.get(f'{BASE_URL}/facts/random')
    assert response.status_code == 200
    assert 'text' in response.json()
    
def test_get_all_cat_facts():
    response = requests.get(f'{BASE_URL}/facts')
    assert response.status_code == 200
    facts = response.json()
    assert isinstance(facts, list)

def test_invalid_route():
    response = requests.get(f'{BASE_URL}/invalid_route')
    assert response.status_code == 404
    print(response.text)
