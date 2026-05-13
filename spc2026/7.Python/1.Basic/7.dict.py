# 딕셔너리
# 키와 값의 쌍을 저장하는 자료구조
# 키는 중복될 수 없음
# 값은 중복될 수 있음
# 키는 문자열, 숫자, 튜플 등 변경 불가능한 자료형만 사용 가능
# 값은 모든 자료형 사용 가능
# 딕셔너리 생성
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}

# 딕셔너리 추가
person["email"] = "john@example.com"
print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

# 딕셔너리 수정
person["age"] = 31
print(person) # {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# 딕셔너리 삭제
del person["email"]
print(person) # {'name': 'John', 'age': 31, 'city': 'New York'}

print(person.pop("age")) # 해당 키의 값을 반환하고 삭제

# 리스트 [] 대괄호 사용, 수정 가능 리스트
# 튜플 () 소괄호 사용, 읽기 전용 리스트
# 딕셔너리 {} 중괄호 사용, 키 벨류 리스트

