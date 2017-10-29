print('if条件判断,注意不要少些了冒号:')
print('if...elif...elif...else...')

birth = input('输入生日(年):')

birth = int(birth)

if(birth < 2000):
    print('00前')
elif(birth == 2000):
    print('00')
else:
    print('00后')