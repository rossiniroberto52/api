import requests

def test_should_get_status_code_200():
    r = requests.get('localhost:8000/')
    response = r.json()
    print(response)
    
test_should_get_status_code_200()