from main import app
from utils.util import read_convert_to_jsonl
from fastapi.testclient import TestClient

# Load TestClient object
client = TestClient(app)

# Test Service-1
def test_get_entities():
    # Load and convert json to jsonl
    data = read_convert_to_jsonl('resume_labels.json')
    # Iterate over all json-lines of json object
    for payload in data:
        # Send request through client
        response = client.post("/get_entities", json=payload)
        # Check for successful request execution
        assert response.status_code == 200

# Test Service-2
def test_transform_json_to_csv():
    # Send request through client
    response = client.get("/transform_json_to_csv/resume_labels.json")
    # Check for successful request execution
    assert response.status_code == 200