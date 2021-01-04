from compare_mp3 import compare
import os
from datetime import datetime
now = datetime.now()
list = os.listdir('.')
x = 0
y = -1
while x < 1:
    x = (x+1)
    while y < 1818:
        y = (y+1)
        mp3data = open("mp3.txt","a+", encoding='utf-8' )
        append = list[y]
        mp3data.write(append + "\n")
        mp3data.close()
        print(now)

print('Program Finished')
