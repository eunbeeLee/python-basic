print('%d'%15)
print('{}'.format(15)) # 데이터를 구분하지 않는다

fruit = 'apple'
count = 10
print('나는 {0}를 {1}개 구입했습니다.'.format(fruit,count))
print('나는 {1}를 {0}개 구입했습니다.'.format(fruit,count))
print('나는 {1}를 {1}개 구입했습니다.'.format(fruit,count))

print('{0}, {0}, {0}'.format(count))

print('['+'{0:5}'.format(2)+']') # 5자리 출력, 출력 자리수를 정하면 오른쪽 정렬
print('['+'{0:<5}'.format(2)+']') # 왼쪽 정렬
print('['+'{0:>5}'.format(2)+']') # 오른쪽정렬
print('['+'{0:^5}'.format(2)+']') # 가운데정렬

print('['+'{0:.2f}'.format(3.146543213)+']') # 실수 자리수 지정 출력




