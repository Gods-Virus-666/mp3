mp3data = open('mp3.txt','r+')
for line in mp3data:
    line = line.rstrip()
    if line.find('(1)') == -1: continue
    print(line)
    f=open('mp3duplicates.txt','a+')
    f.write(line + '\n')
    f.close()
mp3data = open('mp3.txt','r+')
for line1 in mp3data:
    line1 = line1.rstrip()
    if line1.find('(2)') == -1: continue
    print(line1)
    f=open('mp3duplicates.txt','a+')
    f.write(line1 + '\n')
    f.close()
print('Program Finished')


