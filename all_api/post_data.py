import requests
def post_api(base_url,name,department,salary):
    data = {"name":name,"department":department,"salary":salary}
    response = requests.post(base_url + "/employees",json=data)
    return response

