import json
import csv
import requests

# URL of the JSON file
JSON_URL = "https://raw.githubusercontent.com/seanprashad/leetcode-patterns/main/src/data/questions.json"

# CSV output file
OUTPUT_CSV = "leetcode_problems.csv"

# Fetch JSON data from URL
response = requests.get(JSON_URL)
data = response.json()

# Define the CSV structure
csv_headers = ["id", "name", "link", "difficulty", "pattern"]

# Open CSV file for writing
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)  # Write headers
    
    # Extract problems data (data['data'] is a list)
    for problem in data["data"]:
        problem_id = problem.get("id", "")
        name = problem.get("title", "")
        slug = problem.get("slug", "")
        link = f"https://leetcode.com/problems/{slug}"
        difficulty = problem.get("difficulty", "")
        pattern = ", ".join(problem.get("patterns", []))  # Concatenate patterns
        
        # Write row to CSV
        writer.writerow([problem_id, name, link, difficulty, pattern])

print(f"CSV file '{OUTPUT_CSV}' has been created successfully.")
