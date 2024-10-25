from framework.api_helpers import get_request, post_request

def test_get_user_data():
    url = "https://api.example.com/users/1"
    user_data = get_request(url)
    assert user_data["id"] == 1
    assert user_data["name"] == "John Doe"
