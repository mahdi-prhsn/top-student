import io
file = open('practice.txt', 'wt')
for i in range(5):
    code = int(input('enter code: '))
    name = input('enter ur name: ')
    mark = int(input('enter ur mark: '))
    if code > 0:
        code = str(code) + '\n'
        mark = '\n' + str(mark) + '\n'
        file.write(code)
        file.write(name)
        file.write(mark)
    else:
        break
file.close()
