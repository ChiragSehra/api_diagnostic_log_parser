import json
import csv
import pandas as pd

# shards.json
# Open the file for reading
with open('api-diagnostics-20230404-101458/shards.json', 'r') as f:
    # Load the contents of the file as a JSON object
    data = json.load(f)

# # Iterate over the list of dictionaries and print each key-value pair
# for item in data:
#     for key, value in item.items():
#         print(f"{key}: {value}")
#     print()  # Print an empty line between items

# Convert to DataFrame
df = pd.json_normalize(data)

# Write to CSV file
df.to_csv('data.csv', index=False)
