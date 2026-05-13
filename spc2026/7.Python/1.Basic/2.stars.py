print('*')
print('**')
print('***')
print('****')
print('*****')

print('\n - 1 - ')
for i in range(1, 6): # 1부터 5까지 반복, 5를 포함하지 않음
  print("*" * i) # i번 반복하여 * 출력

print('\n - 2 - ')
for i in range(1, 6):
  print(" " * (5 - i) + "*" * i) # 5 - i 만큼 공백을 출력하고 i번 반복하여 * 출력

print('\n - 3 - ')
for i in range(1, 6):
  print(" " * (5 - i) + "*" * (i * 2 - 1)) # 5 - i 만큼 공백을 출력하고 i번 반복하여 * 출력하고 5 - i 만큼 공백을 출력