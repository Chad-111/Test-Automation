import requests

def get_dog_facts(limit=12):
    """Fetch a list of dog facts from the Dog Facts API."""
    url = f"https://dogapi.dog/api/v2/facts?limit={limit}"
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the response as JSON
    else:
        response.raise_for_status()  # Raise an error for bad status codes
