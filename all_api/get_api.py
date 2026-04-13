import requests
def get_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response.json())
    assert response.status_code == 200