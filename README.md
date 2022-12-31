# Lab Assignment - Objectways

## Directory structure
- `utils`: util.py - helper functions for main underlying functionalities of each service.
- `results`: output files - converted json to jsonl and csv from json.
- `main.py`: FastAPI app with 2 services: /get_entities & /transform_json_to_csv
- `test_main.py`: Simple unit-test with pytest using fastapi TestClient
- `send_requests`: Sending appropriate request for each service and printing results