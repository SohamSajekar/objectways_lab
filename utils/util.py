import json
import pandas as pd


def read_convert_to_jsonl(path):
    data = []
    with open(path, 'r') as f:
        json_data = json.load(f)
    with open('results/converted.jsonl', 'w') as outfile:
        for entry in json_data:
            json.dump(entry, outfile)
            outfile.write('\n')
    with open("results/converted.jsonl") as f1:
        for line in f1:
            json_line = json.loads(line)
            data.append(json_line)
    return data

def count_entities(data):
    filenames, entity_types, entity_count, result = [], [], [], []
    if 'file_name' in data and 'annotations' in data:
        if 'tags' in data['annotations']:
            etypes = []
            tags = data['annotations']['tags']
            for tag in tags:
                etypes.append(tag['type'])
            unique_etypes = list(set(etypes))
            entity_types.extend(unique_etypes)
            entity_count.extend([etypes.count(etype) for etype in unique_etypes])
            filenames.extend([data['file_name']] * len(unique_etypes))
            for idx, type in enumerate(entity_types):
                result.append({type: entity_count[idx]})
    if len(result) == 0:
        return [0], [0], [0], [0]
    return filenames, entity_types, entity_count, result

def flatten(list):
    return [item for sublist in list for item in sublist]

def save_csv(filenames, entity_types, entity_count):
    savepath = 'results/resume_labels.csv'
    col1, col2, col3 = flatten(filenames), flatten(entity_types), flatten(entity_count)
    df = pd.DataFrame({'File Name': col1, 'Entity Type': col2, 'Count of Entities': col3})
    df.to_csv(savepath, index=False)
    return savepath, df