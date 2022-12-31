import json
import pandas as pd


# Function to convert json to jsonl
def read_convert_to_jsonl(path):

    # Initialize empty list for storing each jsonline as json object
    data = []

    # Load json file
    with open(path, 'r') as f:
        json_data = json.load(f)

    # Convert and save json into json-line format, ".jsonl"
    with open('results/converted.jsonl', 'w') as outfile:
        for entry in json_data:
            json.dump(entry, outfile)
            outfile.write('\n')

    # Read each json line as seperate json object
    with open("results/converted.jsonl") as f1:
        for line in f1:
            json_line = json.loads(line)
            data.append(json_line)

    return data

# Function to parse json and fetch entities and their count for each file
def count_entities(data):

    # Initialize empty lists
    filenames, entity_types, entity_count, result = [], [], [], []

    # Sanity check for key('file_name','annotations','tags') in dict/payload
    if 'file_name' in data and 'annotations' in data:
        if 'tags' in data['annotations']:
            etypes = []
            # Load all tage available
            tags = data['annotations']['tags']

            # Iterate over tags and fetch the 'type' entity
            for tag in tags:
                etypes.append(tag['type'])

            # Find unique types
            unique_etypes = list(set(etypes))
            # Store entities and their counts in initialized lists
            entity_types.extend(unique_etypes)
            entity_count.extend([etypes.count(etype) for etype in unique_etypes])
            filenames.extend([data['file_name']] * len(unique_etypes))

            # Generate output in json format for service1(/get_entities) of fastapi
            for idx, type in enumerate(entity_types):
                result.append({type: entity_count[idx]})

    # If sanity check failed, return zero list: represents nan values
    if len(result) == 0:
        return [0], [0], [0], [0]

    return filenames, entity_types, entity_count, result

# Function to convert nested list to flattened list
def flatten(list):
    return [item for sublist in list for item in sublist]

# Function to save csv for parsed json payload (service2: /transform_json_to_csv)
def save_csv(filenames, entity_types, entity_count):

    # Create path to save csv file
    savepath = 'results/resume_labels.csv'
    # Flatten entity lists from parsed json
    col1, col2, col3 = flatten(filenames), flatten(entity_types), flatten(entity_count)
    # Create dataframe
    df = pd.DataFrame({'File Name': col1, 'Entity Type': col2, 'Count of Entities': col3})
    # Save dataframe to csv file
    df.to_csv(savepath, index=False)

    return savepath, df