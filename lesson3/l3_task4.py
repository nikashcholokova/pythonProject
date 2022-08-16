#list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

list_of_six= list(range(100, 197, 6))
print(list_of_six)

for number in list_of_six:
    if (number % 5 == 0) and (number < 150):
        print(number)


