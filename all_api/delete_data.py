import requests
def delete_api(base_url):
    response = requests.delete(base_url + "/employees/4")
    return response