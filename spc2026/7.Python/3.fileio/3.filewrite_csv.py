import csv

data = [
  ["name", "age", "city"],
  ["John", 30, "New York"],
  ["Jane", 25, "Los Angeles"],
  ["Jim", 35, "Chicago"]
]

with open("data.csv", "w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerows(data)


data2 = [
  {"name": "John", "age": 30, "city": "New York"},
  {"name": "Jane", "age": 25, "city": "Los Angeles"},
  {"name": "Jim", "age": 35, "city": "Chicago"}
]

with open("data2.csv", "w", newline="", encoding="utf-8") as file:
  writer = csv.DictWriter(file, fieldnames=data2[0].keys())
  writer.writeheader()
  for row in data2:
    writer.writerow(row)