students = {
    '민준': 85,
    '서연': 92,
    '지후': 74,
    '하은': 99,
    '도윤': 68,
    '예준': 81,
    '서준': 95,
    '지아': 77,
    '유진': 88,
    '현우': 90
}

print(students)

def get_a_student(students): # 90점 이상인 학생들의 이름을 리스트로 반환하는 함수
  a_students = []
  for student, score in students.items(): # 딕셔너리의 키와 값을 가져옴
    if score >= 90:
      a_students.append((name, score))
  return a_students # 90점 이상인 학생들의 이름을 리스트로 반환

print(get_a_student(students)) # 90점 이상인 학생들의 이름을 출력