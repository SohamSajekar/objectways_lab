from main import app
from utils.util import read_convert_to_jsonl
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_entities():
    data = read_convert_to_jsonl('resume_labels.json')
    for payload in data:
        response = client.post("/get_entities", json=payload)
        assert response.status_code == 200

def test_transform_json_to_csv():
    response = client.post("/transform_json_to_csv/resume_labels.json")
    assert response.status_code == 200