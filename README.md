# Lab Assignment - Objectways

## Directory structure
- `utils/`: util.py - helper functions for main underlying functionalities of each service.
- `results/`: output files - converted json to jsonl and csv from json.
- `main.py`: FastAPI app with 2 services: /get_entities & /transform_json_to_csv
- `test_main.py`: Simple unit-test with pytest using fastapi TestClient
- `send_requests`: Sending appropriate request for each service and printing results

## Checklist and executed functionalities
1. Convert the JSON file to Json line with each set as a json line. ***status: completed***
2. Calculate number of instances of entities per Json line. ***status: completed***
3. Create a FastAPI/Flask or DJango Service with 2 services. ***status: completed***
4. Calculate (Precision/Recall/F1/Kappa Score) for annotator(Predicted Label) and reviewer(Ground Truth Label) ***status: incompleted***
5. `BONUS` - Write Unit test with pytest. ***status: completed***