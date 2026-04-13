import requests
def get_api(base_url):
    response = requests.get(base_url  + "/posts")
    # print(response.json())
    return response
