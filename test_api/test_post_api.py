from all_api.post_api import post_api
def test_post_api(base_url):
    response = post_api(base_url)
    assert response.status_code == 201