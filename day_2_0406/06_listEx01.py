a = [1,2,['a','b',['Life','is']]]

print(a[2][2][0])

a = [2,4,6,8,'hi~~',[1,3,5], 2.5]
print(a[4])

# mix_value와 value에서 one, two 출력
mix_value = [1, 2, 3, 'one', 'two', 'three']
value = [1, 2, 3, ['one', 'two', 'three']]
print(mix_value[3:5])
print(value[3][:2])
