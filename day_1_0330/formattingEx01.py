n1 = 10
n2 = 20

print('숫자출력 : %d' % n1)
print('n1 : %d, n2 : %d' % (n1, n2))

# 자리수 정하기
print("%5d" % n1)
print("%.5d" % n1)
print("%05d|" % n1) # 5자리 왼쪽 정렬
print("%-5d|" % n1) # 5자리 오른쪽 정렬
print("%+5d|" % n1) # +기호보여주기

# 8진수, 16진수의 서식문자
num1 = 10
print('%d, %#o, %#x'%(num1, num1, num1))

# 실수
print("%f" % 3.145362465464353)
print("%.2f" % 3.145362465464353)
print("%.0f%%입니다" % 3.145362465464353)  # %% 두번 쓰면 %그대로 출력 가능


print("사과 2개")
print("사과 %d 개" % 2)

apple = 5
print("사과 %d 개" % apple)
pear = 4
print("사과 %d개, 배 %d 개" % (apple, pear))

fruit1 = "사과"
fruit2 = "배"
print("%s 3개" % fruit1)

#문제

apple = 5
pear = 4
fruit1 = "사과"
fruit2 = "배"

print("형태 : %d개, %s %d개" % (pear, fruit1, apple))