import re
N=input()
for i in range(N):

if re.match(r'[789]\d{9}$',raw_input()):   
    print 'YES'  
else:  
    print 'NO'
