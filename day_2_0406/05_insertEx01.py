# 사용자가 입력한 값의 2배 된 값을 출력
print('출력시작')
# a = int(input("값을 입력하세요: "));
# print(2*a)

# 퀴즈
# su1, su2 변수에 정수 2개를 입력 받아서 저장 ->출력
# 출력형태 : su1 :10, su2 : 20
# su1 = int(input('su1의 값을 입력하세요'))
# su2 = int(input('su2의 값을 입력하세요'))
# print('su1 : %d, su2 : %d' % (su1,su2))
# print('su1 : {}, su2 : {}'.format (su1,su2))

# 숫자 데이터를 하나 입력(정수, 실수) eval 함수
# num = eval(input("숫자 데이터 입력 : "))
# print(num)

# 입력 한번에 받아보기
# a, b = input('숫자 데이터 하나 입력: ').split(",")
# print(a)
# print(b)

# map 활용
# a, b = map(float,input('숫자 데이터 두개 입력: ').split(","))
# print(type(a))
# print(type(b))

#hi hello를 각 변수에 저장
# s, t = input('문자열 입력:').split(",")
# print('s : {}-문자수 : {}, t : {}-문자수 : {}'.format(s, len(s), t, len(t)))

# de = int(input('10진수 입력'))
# print('de : ',de)
# oct = int(input('10진수를 8진수로 변환:'), 8)
# print('oct : ',oct)
# hex = int(input('10진수를 16진수로 변환'), 16)
# print('hex : ',hex)

tuple_value = eval(input('값 입력(1,2,3):'))
print(tuple_value[0])
print(type(tuple_value))

print('출력완료')
