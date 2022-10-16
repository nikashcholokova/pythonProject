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
sorted_elems = sorted(elements_to_operate)
for current in sorted_elems[0:-2]:
    if current == sorted_elems[-1]:
        count_max_duplicates += 1
    if current % 2 == 1:
        count_odds += 1

print(elements_to_operate)
print("Items count = " + str(len(elements_to_operate)))
print("Sum = " + str(sum(elements_to_operate)))
print("Prod = " + str(math.prod(elements_to_operate)))
print("Avg = " + str(sum(elements_to_operate) / len(elements_to_operate)))
print("Max index = " + str(elements_to_operate.index(max(elements_to_operate))))
print("Odd count = " + str(count_odds) +
      "\nEven count = " + str((len(elements_to_operate) - count_odds)))
print("2nd Max = " + str(sorted(elements_to_operate)[-2]))
print("Max duplicates = " + str(count_max_duplicates))