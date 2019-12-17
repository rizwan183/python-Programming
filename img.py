import glob
import os
address=[]
print(os.listdir())
a=glob.glob('*.png')
print(glob.glob('*.py'))
for i in a:
    ##print(i)
    #print(os.path.abspath(i))
    address.append(os.path.abspath(i))
print(address)
f=open("ab.py","w")
for j in address:
    f.write(os.path.abspath(j))
f.close()
