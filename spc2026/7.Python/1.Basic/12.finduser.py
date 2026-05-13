users = [
    {"name": "김민정", "age": 28, "location": "Toronto", "car": "Tesla Model 3"},
    {"name": "Sophia", "age": 34, "location": "Vancouver", "car": "BMW X5"},
    {"name": "Minjun", "age": 25, "location": "Seoul", "car": "Hyundai Avante"},
    {"name": "Emma", "age": 31, "location": "New York", "car": "Audi A4"},
    {"name": "Lucas", "age": 22, "location": "Sydney", "car": "Toyota Corolla"},
    {"name": "Olivia", "age": 29, "location": "London", "car": "Mercedes-Benz C-Class"},
    {"name": "김수아", "age": 37, "location": "Busan", "car": "Kia Sportage"},
    {"name": "Daniel", "age": 40, "location": "Chicago", "car": "Ford Explorer"},
    {"name": "Hannah", "age": 26, "location": "Berlin", "car": "Volkswagen Golf"},
    {"name": "Ethan", "age": 36, "location": "Tokyo", "car": "Nissan Altima"}
]

def find_user(name):
  for user in users:
    # if user["name"] == name: # 이름이 정확히 일치하는 경우
    if user["name"].startswith(name): # 이름이 시작하는 문자가 일치하는 경우
      print(user)
  return None # 찾지 못한 경우 None을 반환

# find_user("김") # 김으로 시작하는 사용자를 찾음

def find_user_and_return(name):
  found_users = [] # 찾은 사용자들을 저장할 리스트
  for user in users:
    if user["name"].startswith(name):
      found_users.append(user)
  return found_users # 찾은 사용자들을 리스트로 반환

found_users = find_user_and_return("김")
# print(found_users) # 김으로 시작하는 사용자들을 출력

def find_users2(name, age):
  found_users = [] # 찾은 사용자들을 저장할 리스트
  for user in users:
    if user["name"].startswith(name) and str(user["age"]).startswith(age):
      found_users.append(user)
  return found_users # 찾은 사용자들을 리스트로 반환

print(find_users2("김", "2")) # 김으로 시작하는 20대 사용자들을 출력

