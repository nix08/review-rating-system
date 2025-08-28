import os
import json

# Paths
input_path = 'ml_model/data/Electronics.jsonl'  # Your full dataset
output_dir = 'ml_model/data/chunks/'       # Where chunks will be saved
os.makedirs(output_dir, exist_ok=True)

# Settings
chunk_size = 100000
chunk_count = 0
buffer = []

# Read and split
with open(input_path, 'r', encoding='utf-8') as infile:
    for line_num, line in enumerate(infile, start=1):
        buffer.append(json.loads(line))
        if line_num % chunk_size == 0:
            with open(f'{output_dir}chunk_{chunk_count}.json', 'w', encoding='utf-8') as outfile:
                json.dump(buffer, outfile, ensure_ascii=False, indent=2)
            print(f"Saved chunk_{chunk_count}.json with {chunk_size} records")
            buffer = []
            chunk_count += 1

# Save remaining records
if buffer:
    with open(f'{output_dir}chunk_{chunk_count}.json', 'w', encoding='utf-8') as outfile:
        json.dump(buffer, outfile, ensure_ascii=False, indent=2)
    print(f"Saved final chunk_{chunk_count}.json with {len(buffer)} records")