a = str(input("Введите Фамилию Имя Отчество и номер телефона "))
path = 'input.txt'
f = open(path,'r',encoding='utf-8')
temp = f.read().split('\n') 

 
for i in temp :
    if a in i:
        print(i)
        break
else:
    print('Такого типа нет')