from all_api.put_data import put_api
import pytest
@pytest.mark.parametrize("name",["kamal"])
def test_put_api(base_url,name):
    response = put_api(base_url,name)
    assert response.status_code == 200