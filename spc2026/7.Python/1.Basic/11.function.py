
def add_numbers(a, b):
  # 이 함수는 인자를 두개 받아서 더한 값을 반환하는 함수입니다.
  result = a + b
  return result # 더한 값을 반환합니다.

sum = add_numbers(3, 4) # 3과 4를 더한 값을 반환합니다.
print(f'3과 4의 합은 {sum}입니다.') # 3과 4의 합은 7입니다.

def add_numbers2(a, b):
  return a, b, a + b

input1, input2, sum = add_numbers2(3, 4) # 3과 4를 더한 값을 반환합니다.
print(f'{input1}과 {input2}의 합은 {sum}입니다.') # 3과 4의 합은 7입니다.

def calculate_all(a, b):
  # 이 함수는 인자를 두개 받아서 더한 값, 뺀 값, 곱한 값, 나눈 값을 반환하는 함수입니다.
  addition = a + b # 더한 값
  subtraction = a - b # 뺀 값
  multiplication = a * b # 곱한 값
  division = a / b # 나눈 값
  return addition, subtraction, multiplication, division # 더한 값, 뺀 값, 곱한 값, 나눈 값을 반환

add, sub, mul, div = calculate_all(3, 4) # 3과 4를 더한 값, 뺀 값, 곱한 값, 나눈 값을 반환합니다.
print(f'더한 값: {add}, 뺀 값: {sub}, 곱한 값: {mul}, 나눈 값: {div}') # 더한 값: 7, 뺀 값: -1, 곱한 값: 12, 나눈 값: 0.75

add, _, mul, _ = calculate_all(5, 6) # 5와 6를 더한 값, 뺀 값은 무시하고 곱한 값을 반환합니다.
print(f'더한 값: {add}, 곱한 값: {mul}') # 더한 값: 11, 곱한 값: 30