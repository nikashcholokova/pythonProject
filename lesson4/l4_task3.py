a = int(input('A: '))
b = int(input('B: '))

if a < b:
    for numb in range(a, b + 1):
        print(numb)
elif a > b:
    for numb in range(a, b - 1, -1):
        print(numb)
else:
    print('a=b')
