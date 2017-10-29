str = "python内置的一种数据类型是列表：list。它是一种有序的集合，可以随时添加和删除一种的元素。"
print(str)
classmates = ['maybexss', 'bluer', 'xuxi']
print(classmates)
print('length of clasmates : ', len(classmates))
print('second element is : ', classmates[1])
print('倒数第一个元素是：',classmates[-1])
print('插入一个元素到第三元素中')
classmates.insert(2, 'love you')
print(classmates)
print('删除第三个元素')
classmates.pop(2)
print(classmates)
print('修改元素')
classmates[0] = 'sweeky'
print(classmates)
print('另一种有序列表叫元组。它一旦初始化就不能修改')
classmates = ('sweeky', 'bluer', 'xuxi')
print(classmates)
print('如果tuple中只有一个元素，定义为tuple，则选择在第一个元素后添加逗号')
classmates = (1,)
print(classmates)
print('tuple的不变指的是指向永远不变')
L = [['Apple', 'Google', 'Microsoft'],
     ['Java', 'Python', 'PHP'],
     ['xss', 'wfm', 'xx']]
print('打印Apple:',L[0][0])
print('打印python:', L[1][1])
print('打印xx:', L[2][2])