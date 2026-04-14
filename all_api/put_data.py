import requests
def put_api(base_url,name):
    data = {"name":name}
    response = requests.put(base_url + "/employees/1",json = data)
    return response
def put_api1(base_url,department):
    data = {"department":department}
    response = requests.put(base_url + "/employees/",json = data)
    return response
def put_api2(base_url,salary):
    data = {"salary":salary}
    response = requests.put(base_url + "/employees/",json = data)
    return response
