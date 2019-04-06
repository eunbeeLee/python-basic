# 서식문자 : %c

ch = 'a'

print('문자값 : %c'%ch)
print('문자값 : %s'%ch)

# print('문자값 %d%%'%ch)

print('%-10sjane.' % 'hi')

print('나는 {a}를 {b}개 구입함'.format(a='apple', b=10))

print('{0:<10}'.format('hi'))
print('{0:>10}'.format('hi'))
print('{0:=^10}'.format('hi'))