import requests
from utils.util import read_convert_to_jsonl


def send_request(json_file_path, url, service='transform_json_to_csv'):

    if service == 'transform_json_to_csv':
        # Send GET request to FastAPI
        service2_res = requests.get(url + '/' + json_file_path)
        # result
        print(service2_res.json())
    else:
        # Read json file and convert to json-line format
        data = read_convert_to_jsonl(json_file_path)
        # Send GET request to FastAPI for each json line
        for payload in data:
            service1_res = requests.post(url, json=payload)
            print(service1_res.json())

def main():

    # Json file path location
    json_file_path = 'resume_labels.json'
    # URL for service 1: get_entities
    service1_url = 'http://localhost:8000/get_entities'
    # URL for service 2: transform json to csv
    service2_url = 'http://localhost:8000/transform_json_to_csv'
    # Send requests and print output
    print("Service 1 - get_entities")
    send_request(json_file_path, service1_url, service='get_entities')
    print()
    print("Service 2 - transform_json_to_cv")
    send_request(json_file_path, service2_url, service='transform_json_to_csv')


if __name__ == '__main__':
    main()
