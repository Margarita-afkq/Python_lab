# Task 1
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

print(f'{RED}{" " * 20}{END}')
print(f'{WHITE}{" " * 20}{END}')
print(f'{BLUE}{" " * 20}{END}')
print('' * 10)

# Task 2
print(f'{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}')
print(f'{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}')
print(f'{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}{RED}{" " * 5}{END}{" " * 5}')
print('' * 10)

# Task 3
res = [[0 for i in range(11)] for j in range(21)]

for i in range(21):
    for j in range(11):
        if j * 2 == i and i != 0:
            res[(20 - i) % 20][j] += 1

for i in range(21):
    line = ''
    for j in range(11):
        if j == 0:
            line += '\t' + str(20-i) + '\t'
        else:
            if res[i][j] == 0:
                line += '---'
            if res[i][j] == 1:
                line += '*'
    print(line)
print('\t 0  1  2  3  4  5  6  7  8  9  10')
print('' * 10)
# Task 4
END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

f = [float(i) for i in open('sequence')]

cnt0, cnt1 = 0, 0
for i in range(len(f)):
    if i % 2 == 0:
        cnt0 += abs(f[i])
    else:
        cnt1 += abs(f[i])

cnt0, cnt1 = round(cnt0 // 10), round(cnt1 // 10)

print(f"сум чисел на четных позициях: {SET_COLOR}10m{' '*cnt0}{END}")
print(f"сум чисел на нечетн позициях: {SET_COLOR}18m{' '*cnt1}{END}")
