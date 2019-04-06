a = [1, 2, 3]
b = ['one', 'two', 'three']
print(a, b)
print(a + b)
print(a *3)

a[1] = 5
print(a)

a[0:1] = [2,3,4]
print(a)

a[0:1] = []
print(a)
print('='*20)
del a[1]
print(a)

a.sort()
print(a)

a.reverse()
print(a)

# print('index:',a.index(4))

a.append(7)
print(a)

a.insert(1, 9)
print(a)

a.remove(9)
print(a)

a.pop(1)
print(a)

# quiz
# hi라는 요소(위치가 고정은 아님)를 찾아서 hello로 변경
data = [100, 200, 'hi', 'good', 300]
data[data.index('hi')] = 'hello'
print(data)

a = [1, 2, 3]
b = 'hi'
print(str(a[2]) + b)