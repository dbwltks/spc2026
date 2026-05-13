# 문자열을 변수에 할당하면 string 타입으로 할당된다.
s = "Hello, Python!"
print(s) # Hello, Python!
print(s.lower()) # 모두 소문자로 변경
print(s.upper()) # 모두 대문자로 변경
print(s.capitalize()) # 첫 글자를 대문자로 변경
print(s.title()) # 각 단어의 첫 글자를 대문자로 변경
print(s.swapcase()) # 대문자를 소문자로, 소문자를 대문자로 변경
print(s.strip()) # 앞뒤 공백 제거
print(s.lstrip()) # 왼쪽 공백 제거
print(s.rstrip()) # 오른쪽 공백 제거
print(s.replace("Hello", "Hi")) # Hello를 Hi로 변경
print(type(s)) # <class 'str'>

# 문자열 찾기
print(s.find("Python")) # Python의 인덱스 반환