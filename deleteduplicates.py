import os
import linecache
file = open('mp3duplicates.txt' , 'r')
x=0
while x < 750:
    x =(x+1)
    y = linecache.getline('mp3duplicates.txt', x)
    z = y.rstrip()
    if os.path.exists(z):
        os.remove(z)
        print(z + ' deleted')
    else:
        print('Error song not found')
print('Program Finished')
