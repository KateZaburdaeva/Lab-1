BLUE = 	'\u001b[44m'
WHITE = '\u001b[47m'
RED = '\u001b[41m'
END = '\u001b[0m'

for i in range(4):
    print((BLUE + ' '*4 + END)+(WHITE + ' '*4 + END)+(RED + ' '*4 + END))




WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'

def uzor (size):
    for line in range(size):
        for column in range(size):
            if (line + column) % 2 == 0:
                print((BLACK + ' '*2 + END), end="")
            else:
                print((WHITE + ' '*2 + END), end="")
        print()

print(uzor(3))




def grafic():
    height = 22
    width = 50
    scale_y = height/(width ** 2)
    points = []

    for x in range(width +1):
        y = x ** 2
        if y < height:
            points.append((x, height - y))

    for rad in range(height + 1):
        for col in range(width + 1):
            if (col, rad) in points:
                print("1", end=" ")
            else:
                print(" ", end= " ")
        print()
grafic()




RED = '\u001b[41m'
END = '\u001b[0m'

file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
    list.sort(reverse=False)

less = 0
more = 0 

for i in range(0, len(list)):
    if int(list[i]) > 0:
        less += 1
    elif int(list[i]) < 0:
        more += 1

less = less 
more = more 

# print(list)

print('Больше 0', '(', more, ')', f'{RED}{" " * more}{END}')
print('Меньше 0', '(', less, ')', f'{RED}{" " * less}{END}')

