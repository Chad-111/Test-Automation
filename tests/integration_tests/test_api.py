from framework.api_helpers import get_dog_facts

def test_get_dog_facts():
    facts = get_dog_facts(limit=1)
    
    # Check if the response contains a 'data' key and is a list
    assert "data" in facts
    assert isinstance(facts["data"], list)
    
    # Check if the first fact has the necessary fields
    first_fact = facts["data"][0]
    assert "id" in first_fact
    assert "type" in first_fact and first_fact["type"] == "fact"
    assert "attributes" in first_fact
    assert "body" in first_fact["attributes"]
