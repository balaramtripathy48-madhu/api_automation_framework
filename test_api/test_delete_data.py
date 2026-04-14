from all_api.delete_data import delete_api
def test_delete_data(base_url):
    response = delete_api(base_url)
    assert response.status_code == 200