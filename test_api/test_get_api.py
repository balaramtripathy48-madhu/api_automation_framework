from all_api.get_api import get_api
def test_get_api(base_url):
    response = get_api(base_url)
    assert response.status_code == 200