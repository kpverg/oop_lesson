"""
== iso me
!= not equal
>= grater or equal than
<= 
 not
 or
 and

"""

import numbers


a=4
b=57
if(a>b):
    print("a>b")
elif(a<b):
    print("a<b")
else:
    print("a=b")


newlst=[1,2,3,4,5,6,7,8,9]

for num in newlst:
    if num%2==0:
        print(f"o arithmos {num} einai zigos")
    else:
        print(f"o arithmos {num} einai peritos")
sum=0
for num in newlst:
    sum+=num
print(f"to athroisma ths lstas  einai :{sum}")

x=0
while True:
    if x<=7:
        print(x)
        x+=1
    else:
        break;

