import math

user_input = None
elements_to_operate = []
while user_input != 0:
    user_input = int(input('Please enter an integer number: '))
    if user_input == 0:
        break
    elements_to_operate.append(user_input)

count_max_duplicates = 0
count_odds = 0
maximum = sorted(elements_to_operate)[-1]
max_indexes = []
count = 0
for current in elements_to_operate:
    if current == maximum:
        count_max_duplicates += 1
        max_indexes.append(count)
    if current % 2 == 1:
        count_odds += 1
    count += 1

print(elements_to_operate)
print("Items count = " + str(len(elements_to_operate)))
print("Sum = " + str(sum(elements_to_operate)))
print("Prod = " + str(math.prod(elements_to_operate)))
print("Avg = " + str(sum(elements_to_operate) / len(elements_to_operate)))
print("Max index = " + str(max_indexes))
print("Odd count = " + str(count_odds) +
      "\nEven count = " + str((len(elements_to_operate) - count_odds)))
print("2nd Max = " + str(max(list(filter(maximum.__ne__, elements_to_operate)))))
print("Max duplicates = " + str(count_max_duplicates))
