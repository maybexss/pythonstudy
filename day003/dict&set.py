print('dist study')
d = {'xss': '19920104','wfm': '19891212', 'xx': '20190202'}
print(d['xss'])
print(d)
print('把数据放入dict的方法，除了初始化时指定外，还可以通过key放入')
d['xx'] = '20200202'
print(d)
print('判断key是否在其中，可以通过in判断是否存在:')
print('\'test\' in d', 'test' in d)
print('或者利用dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value')
print('d.get(\'test\'):', d.get('test'))
print('d.get(\'test\', -1):', d.get('test', -1))
print('要删除key,利用pop(key)方法')
print('需要注意的是，dict内部存放的顺序和key放入的顺序是没有关系的')
str = r'''和list比较，dict有以下几个特点：
1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：
1.查找和插入的时间随着元素的增加而增加；
2.占用空间少，浪费内存很少。
所以，dict适用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在python代码中几乎无处不在，正确
使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
呢么dict内部就混乱了。这个通过key计算位置的算法称之为哈希算法(hash)。
要保证hash的正确性，作为key的对象就不能变。在python中，字符串、证书等都是不可变的，
因此，可以放心的作为key，二list是可变的，就不能作为key
'''
print(str)
print('set学习：')
print('要创建一个set，需要一个list作为输入集合')
s = set([1,3,2])
print('set([1,3,,2,2])',s)
print('重复元素自动过滤，顺序也不是按照添加顺序来的')
print('通过add(key)的方法添加元素到set中，可重复添加但无效果')
s.add(4)
print('s.add(4):',s)
print('通过remove(key)方法删除元素')
s.remove(2)
print('s.remove(2):',s)
print('两个set之间可以做数学意义上的交集、并集等操作')
s1 = set([1,2,3])
s2 = set([1,3,4])
print('s1:',s1)
print('s2:',s2)
print('s1&s2:',s1 & s2)
print('s1 | s2:',s1 | s2)