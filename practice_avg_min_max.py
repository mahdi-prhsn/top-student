code = []
name = []
mark = []
s = 0

def search():
    while True:
        c = int(input('search by code: '))
        for i in code:
            if c not in code:
                print('invalid code')
                break
        else:
            in_req_code = code.index(c)
            N = name[in_req_code]
            M = mark[in_req_code]
            print(N.title(),'has got',M,'!')
            print('-'*60) # Just for beauty
            yes = input('wanna do again?')
            print('-'*60) # Just for beauty
            if (yes[0] == 'n' or yes[0] == 'N'):
                break
            


with open ('practice.txt') as file:
    for i in file:
        if (i[0] == '0' or i[0] == '1' or i[0] == '2'):
            content = int(i)
            if 20 >= content >= 0:
                mark.append(content)
            else:
                code.append(content)
        else:
            name.append(i[:-1])


for i in mark :
    s += i
avg = s / 5

print('average: ',avg)
print('-'*60) # Just for beauty
min_mark = min(mark)
max_mark = max(mark)

in_min_mark = mark.index(min_mark)
in_max_mark = mark.index(max_mark)

print('Min and max marks')
print(name[in_min_mark].title(),': ',min_mark)
print(name[in_max_mark].title(),': ',max_mark)
print('-'*60) # Just for beauty


search()

