import requests

def get_request(url, headers=None):
    """Sends a GET request to the specified URL."""
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
    return response.json()  # Return the response as JSON

def post_request(url, data, headers=None):
    """Sends a POST request to the specified URL with the provided data."""
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def put_request(url, data, headers=None):
    """Sends a PUT request to update data at the specified URL."""
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_request(url, headers=None):
    """Sends a DELETE request to the specified URL."""
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code
