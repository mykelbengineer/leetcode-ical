import csv
from ics import Calendar, Event
from datetime import datetime, timedelta

# Path to the CSV file with LeetCode problems
CSV_FILE = "leetcode_problems.csv"
OUTPUT_ICS = "leetcode_daily_schedule.ics"

# Start date for the schedule
start_date = datetime(2025, 1, 3)

# Read problems from the CSV file
problems = []
with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        problems.append({
            "name": row["problem_name"],
            "link": row["link"],
            "difficulty": row["difficulty"],
            "pattern": row["pattern"]
        })

# Create the calendar
calendar = Calendar()

# Assign a problem to each day
current_date = start_date
for problem in problems:
    event = Event()
    event.name = f"Solve: {problem['name']} ({problem['difficulty']})"
    event.description = f"Problem Link: {problem['link']}"
    event.begin = current_date
    event.duration = timedelta(hours=1)  # Set event duration
    calendar.events.add(event)
    current_date += timedelta(days=1)  # Move to the next day

# Save the calendar to an ICS file
with open(OUTPUT_ICS, "w") as file:
    file.writelines(calendar)

print(f"Calendar saved as {OUTPUT_ICS}.")
