#삼항 연산자
print('5가 크다' if 5>3 else '3이크다')
print('5가 크다' if 5<3 else '3이크다')

#변수 num의 값이 10이면 변수 var에 num의 값을 저장, 아니라면 var에 -1을 저장
num = 5
var = num if num == 10 else -1
print('var: ', var)

#문제1
n1 = 10
n2 = 15
result = n1 if n1>n2 else n2
print(result)

#문제 2
value = "양수" if n1>0 else "0 또는 음수"
print(value)
