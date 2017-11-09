import random

checkcode=''

for i in range(4):
    current=int(random.randrange(0,4))
    #字母
    if current == i:
        tmp = chr(random.randint(65,90))
    #数字
    else:
        tmp = random.randint(0,9)
    checkcode+=str(tmp)
print(checkcode)