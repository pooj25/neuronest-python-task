
import csv
import json

input_file = "day2/students.csv"
output_file = "day2/students.json"

try:
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        students = list(reader)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(students, json_file, indent=4)

    print("CSV successfully converted to JSON!")
    print(f"Total students: {len(students)}")
    print(f"JSON file saved at: {output_file}")

except FileNotFoundError:
    print("Error: CSV file not found!")

except PermissionError:
    print("Error: Permission denied while accessing the file!")