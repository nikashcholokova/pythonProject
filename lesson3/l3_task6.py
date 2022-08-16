x1 = int(input('Please enter x1: '))
y1 = int(input('Please enter y1: '))
x2 = int(input('Please enter x2: '))
y2 = int(input('Please enter y2: '))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print('Yes')
else:
    print('No')