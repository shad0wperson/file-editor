import re
import os

files = os.listdir('./')

def replaceStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
       
        str1 = re.sub(r'<img(.*?)/>',r'<p align="center"><img \1/></p>', str)
        
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)

print(files)
for f in files:
    if f.find('.txt') > -1 :
        replaceStr(f)
