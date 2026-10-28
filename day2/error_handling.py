
import json


def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")


def read_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("JSON Data:", data)
    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")


divide_numbers(10, 2)
divide_numbers(10, 0)

read_json_file("day2/students.json")
read_json_file("day2/missing.json")
