# 1. 작은 파일 읽기
with open("file.txt", "r", encoding="utf-8") as file:
  # 여기에서 파일에 문자열을 읽는 코드를 작성합니다.
  content = file.read()
  print("파일 내용:", content)

# 2. Legacy 파일 읽기 / read / close 패턴 (더 이상 사용하지 않음)
# file = open("file.txt", "r", encoding="utf-8")
# content = file.read()
# print("파일 내용:", content)
# file.close()

# 3. 큰 파일 읽기
with open("file.txt", "r", encoding="utf-8") as file:
  # 여기에서 파일에 문자열을 읽는 코드를 작성합니다.
  lines = file.readlines()

  for line in lines:
    print(line)