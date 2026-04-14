import requests
def get_api(base_url):
    response = requests.get(base_url + "/employees")
    # print(response.json())
    return response
