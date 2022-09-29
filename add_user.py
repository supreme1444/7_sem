import csv

keys = ['Last Name','Name','Number']
path = 'add_user.txt'
path2 = 'input.txt'
f = open(path,'r',encoding='utf-8')
temp = f.read().split('\n')
f = open(path2,'r',encoding='utf-8')
temp1 = f.read().split('\n')
if([element for element in temp if element not in temp1]):
    print(temp)
    lines = []
    for elm in temp:
        temp_dict = {}
        person = elm.split(' ')
        #print(person)
        for i in range(len(person)):
            temp_dict[keys[i]] = person[i]
        lines.append(temp_dict)
    csv_file = 'data1.csv'
    f = open(path2,'a',encoding='utf-8')
    temp3 = f.writelines(temp)
    wr = csv.writer(open(csv_file,"a",encoding='utf-8'),quoting=csv.QUOTE_ALL)
    for word in lines :
        wr.writerow([word])
else:
    print("Такой элемент есть")


   