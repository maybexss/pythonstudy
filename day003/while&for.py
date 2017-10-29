print('for...in循环,依次把list或者tuple中的每一个元素迭代出来')
names = ['xss', 'wfm', 'xx']
for name in names:
    print(name)
print('python 中的range()函数')
print('list(range(5)):', list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print('还有一种是while循环')
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
L = ['xss', 'wfm', 'xx']
for name in L:
    print('Hello,',name)
print(L[0],'make love with',L[1],'and then have',L[2])