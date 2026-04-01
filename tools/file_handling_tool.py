import requests
import csv
import json

### use cases
# API data             - json
# Spreadsheet / tables - csv
# Config files         - json
# Data export          - csv


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# get api data, decode respond as python object
data = response.json()

# detect encoding
# print(f"detect encoding: {json.detect_encoding(data)}")



with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # create the header
    writer.writerow(["Name", "Email"])

    # iterate through json response data, add rows
    for user in data:
        writer.writerow([user["name"], user["email"]])