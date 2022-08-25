number_list = [0,12,4,233,109,1,90]
count = 0
for elem in number_list[1:len(number_list)-1]:
    if (elem > number_list[number_list.index(elem)+1]) and (elem > number_list[number_list.index(elem)-1]):
        count+=1
print(count)