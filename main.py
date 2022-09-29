import csv
keys = ['Last Name','Name','Number']
path = 'input.txt'
path2 ='input_copy.txt'

f = open(path,'r',encoding='utf-8')
temp = f.read().split('\n')
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


wr = csv.writer(open(csv_file,"w",encoding='utf-8'),quoting=csv.QUOTE_ALL)
for word in lines :
    wr.writerow([word])

   
  


            




    

