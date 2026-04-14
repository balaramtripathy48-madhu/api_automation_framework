from all_api.post_data import post_api
import pytest
@pytest.mark.parametrize("name,department,salary", [("soumya","it",20000),("abhi","computer",25000),("badal","computer",65000)])
def test_post_api(base_url,name,department,salary):
    response = post_api(base_url,name,department,salary)
    assert response.status_code == 201