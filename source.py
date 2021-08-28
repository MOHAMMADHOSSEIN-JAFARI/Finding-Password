import hashlib
import csv
from collections import OrderedDict 
from hashlib import sha256
def hash_password_hack(input_file_name, output_file_name):
    has = []
    values = []
    name = []
    small_hash= []
    final_pass=[]
    final_name= []
    for i in range(1000,10000):
        i= str(i)
        has.append(sha256(i.encode('utf-8')).hexdigest())
    
    for j in range(1000,10000):
        j=str(j)
        values.append(j)
    
    combine= OrderedDict(zip(has, values))
    with open(input_file_name, newline= '') as f: 
        reader= csv.reader(f)
        for row in reader: 
            n = row[0]
            name.append(n)
            pas= row[1]
            small_hash.append(pas)
            
    f.close()
    name_has=  OrderedDict(zip(small_hash, name))
    
    for z in has:
        for w in small_hash :
            if z== w:
                final_pass.append(combine[z])
                final_name.append(name_has[w])
    mixture= OrderedDict(zip(final_name, final_pass))
                
                
    
    
    with open(output_file_name, 'w', newline= '') as file:
        writer = csv.writer(file, delimiter=',')
        for k,v in mixture.items():
            writer.writerow([k , v])
    file.close()

    
    