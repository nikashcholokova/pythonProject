x = float(input('x: '))
y = float(input('y: '))
day = 1
while x < y:
    x = x*1.1
    if x >= y:
        break
    day += 1

print(day)
