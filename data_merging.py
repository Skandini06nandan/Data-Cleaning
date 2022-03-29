import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

q1 = []
q2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        q1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        q2.append(i)

h1 = q1[0]
h2 = q2[0]

p_q1 = q1[1:]
p_q2 = q2[1:]

h = h1+h2

p_d =[]

for i in p_q1:
    p_d.append(i)
for j in p_q2:
    p_d.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)