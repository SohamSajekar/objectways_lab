import requests
from ..utils.util import read_convert_to_jsonl

json_file_path = 'resume_labels.json'
data = read_convert_to_jsonl(json_file_path)
service1_url = 'http://localhost:8000/get_entities'
service2_url = 'http://localhost:8000/transform_json_to_csv'
print("Service-1 Output:")
for payload in data:
    # print(payload['file_name'])
    service1_res = requests.get(service1_url, json=payload)
    print(service1_res.json())
print()
service2_res = requests.get(service2_url + '/' + json_file_path)
print("Service-2 Output:")
print(service2_res.json())
