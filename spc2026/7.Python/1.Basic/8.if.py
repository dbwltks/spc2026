print('--- if 구문 ---')

score = 85
if score >= 90:
  # print('성적은 A 입니다.')
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
else:
  grade = 'F'

print(f'당신의 성적은 {grade}입니다.')


month = 7
if month in [12, 1, 2]:
  season = '겨울'
elif month in [3, 4, 5]:
  season = '봄'
elif month in [6, 7, 8]:
  season = '여름'
elif month in [9, 10, 11]:
  season = '가을'
else:
  season = '알 수 없는 계절'

print(f'{month}월은 {season}입니다.')

height = 170
weight = 70
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
  status = '저체중'
elif bmi < 25:
  status = '정상'
elif bmi < 30:
  status = '과체중'
else:
  status = '비만'

print(f'당신의 키는 {height}cm, 몸무게는 {weight}kg, BMI는 {bmi}입니다. {status}입니다.')

username = 'admin'
password = '1234'

if username and password: # username과 password가 모두 있으면 True, 하나라도 없으면 False
  if username == 'admin' and password == '1234':
    print('관리자로 로그인 성공했습니다.')
  elif username == 'user' and password == '1234':
    print('일반 사용자로 로그인 성공했습니다.')
  else:
    print('아이디 또는 비밀번호를 확인해주세요.')
else:
  print('아이디 또는 비밀번호를 입력해주세요.')