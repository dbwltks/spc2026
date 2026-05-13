x = 5
y = 3

print(x + y) # x와 y를 더하기
print(x - y) # x에서 y를 빼기
print(x * y) # x와 y를 곱하기
print(x / y) # x를 y로 나눈 몫
print(x % y) # x를 y로 나눈 나머지
print(x ** y) # x의 y제곱
print(x // y) # x를 y로 나눈 몫(나머지 버림)
print(x ** 0.5) # x의 제곱근(루트)

print(x > y) # x가 y보다 큰지
print(x < y) # x가 y보다 작은지
print(x >= y) # x가 y보다 크거나 같은지
print(x <= y) # x가 y보다 작거나 같은지
print(x == y) # x와 y가 같은지
print(x != y) # x와 y가 다른지

print(x > y and x < y) # x가 y보다 크고 x가 y보다 작은지
print(x > y or x < y) # x가 y보다 크거나 x가 y보다 작은지
print(not x > y) # x가 y보다 크지 않은지
print(not x < y) # x가 y보다 작지 않은지
print(not x >= y) # x가 y보다 크거나 같지 않은지
print(not x <= y) # x가 y보다 작거나 같지 않은지
print(not x == y) # x와 y가 같지 않은지
print(not x != y) # x와 y가 다른지 않은지

print(hex(x)) # 0xa

x = -10
print(x) # -10
print(abs(x)) # 10
print(pow(x, 2)) # 100
print(pow(x, 2, 3)) # 1
print(pow(x, 2, 3)) # 1

y = 4.5
print(y) # 4.5
print(int(y)) # 4


# 비트 연산자(AND, OR, XOR, NOT, SHIFT)
x = 5
y = 3
print(x & y) # 5 = 101, 3 = 011, 101 & 011 = 001 = 1
print(x | y) # 5 = 101, 3 = 011, 101 | 011 = 111 = 7
print(x ^ y) # 5 = 101, 3 = 011, 101 ^ 011 = 110 = 6
print(~x) # 5 = 101, ~101 = 010 = 2


print(x << 1) # 5 = 101, 101 << 1 = 1010 = 10
print(x >> 1) # 5 = 101, 101 >> 1 = 010 = 2