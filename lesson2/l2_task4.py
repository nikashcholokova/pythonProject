years = int(input('Please enter an integer number:'))
if(years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
         print ('Yes')
else:
         print ('No')
