import requests
from ..utils.util import read_convert_to_jsonl

json_file_path = 'resume_labels.json'
data = read_convert_to_jsonl(json_file_path)
service1_url = 'http://localhost:8000/get_entities'
for payload in data:
    service1_res = requests.get(service1_url, json=payload)
    print(service1_res.json())
