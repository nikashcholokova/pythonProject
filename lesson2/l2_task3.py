time_for_vasia = int(input('Пожалуйста, введите время:'))
speed_for_vasia = int(input('Пожалуйста, введите скорость:'))
s = int(time_for_vasia * speed_for_vasia)
v = speed_for_vasia
t = time_for_vasia
if(v>0 and t>0) and (v*t < 100):
    print(int(s))
elif s == 0 :
    print('Вася всё это время стоял на месте')
elif v*t >= 100:
    print('Вася проехал дистанцию')
else:
    print('Вася поехал не в ту сторону')