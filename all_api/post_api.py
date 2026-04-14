import requests
def post_api(base_url):
    data = {"userId": 2,
             "id": 5,
            "title": "meri title",
            "body":"anything"}
    response = requests.post(base_url + "/posts",json=data)
    return response
