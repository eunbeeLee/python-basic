var = "  Hello  "
print("문자열의 길이(len) : ", len(var))
print("문자 찾기(count): ", var.count('l'))
print("문자 찾기(count): ", "hi~~".count('h'))

# 공백 제거
print(var)
print('왼쪽 공백 제거(lstrip()):', var.lstrip())
print('오른쪽 공백 제거(rstrip()):', var.rstrip()+"|")
print('양쪽 공백 제거(rstrip()):', "|"+var.strip()+"|")

print('대문자: ', var.upper())
print('소문자: ', var.lower())

print('e찾기: ', var.find('e'))
# print('e찾기: ', var.index('e'))

print('a로 변경:', var.replace('el', 'a'))
print('문자열 나누기:', var.split(','))
print('문자삽입: ', '~'.join(var))

# 문제
quiz = "Time is too fast."
index = quiz.find("too")
print("too : ", quiz[index:index+len("too")])
