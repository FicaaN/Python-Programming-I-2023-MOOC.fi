word = input("Word: ")

if len(word) == 28:
    print('*' * 30)
    print('*' + word + '*')
    print('*' * 30)
elif len(word) < 28 and len(word) % 2 == 0:
    fill = 28 - len(word) 
    print('*' * 30)
    print('*' + ' ' * (fill // 2) + word + ' ' * (fill // 2) + '*')
    print('*' * 30)
elif len(word) < 28 and len(word) % 2 != 0:
    fill = 27 - len(word) 
    print('*' * 30)
    print('*' + ' ' * (fill // 2) + word + ' ' * (fill // 2) + ' ' + '*')
    print('*' * 30)