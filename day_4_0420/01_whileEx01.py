num = 1

while num < 5:
    print("num:", num)
    num += 1

num = 1
while True:
    print("num:", num)
    num +=1
    if num == 3:
        break

# ====================================================
# continue 는 조건식이 맞을 떄 실행하지 않고 지나가기

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print("num : ", num)



#  퀴즈 구구단 만들기
num = int(input("단을 입력하세요"))
timesNum = 1
while timesNum < 10:
    print("%d * %d = %d" % (num, timesNum, num*timesNum))
    timesNum += 1

# 1부터 10까지 더한 수 출력
result = 0
num = 1
while num <= 10:
    result += num
    num += 1
print("1~10 누적합 :", result)