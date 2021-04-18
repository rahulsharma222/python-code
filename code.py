import os


orig = open('a.csv','r')
new = open('b.csv','r')


bigb = set(new) - set(orig)

print(bigb)


with open('uncommon.csv', 'w') as file_out:
    for line in bigb:
        file_out.write(line)

a.close()    
b.close()    
file_out.close()
