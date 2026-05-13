numbers = [1, 2, 3, 4, 5]

# for num in range(1, 6)
# for num in [1, 2, 3, 4, 5]
for num in numbers:
  if num % 2 == 0:
    print(f'숫자 {num}은 짝수입니다.')
  else:
    print(f'숫자 {num}은 홀수입니다.')

even_count = 0
odd_count = 0

for num in numbers:
  if num % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f'짝수의 개수는 {even_count}개입니다.')
print(f'홀수의 개수는 {odd_count}개입니다.')

n = 10
count = 0

for i in range(n):
  for j in range(n):
    count += 1

print(f'1부터 {n}까지의 합은 {count}입니다.')

start_time = time.time()

# 코드의 시간 복잡도는 O(n^4)입니다.
for i in range(n):
  for j in range(n):
    for k in range(n):
      for l in range(n):
        count += 1

end_time = time.time()
exec_time = end_time - start_time

print(f'1부터 {n}까지의 합은 {count}입니다. 실행 시간: {exec_time}초')