import os
import time
import random
import string
# get the argument passed

count = 0

while True:
    while count<24:
        roa=random.choice(string.ascii_letters)
        roc=random.randint(1,4)
        print('\033[9'+str(roc)+'m',roa,end='')
        count+=1
    count=0
    print('')
    time.sleep(0.04)