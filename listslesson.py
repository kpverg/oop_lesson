mylst1=[1,"petros",3]
mylt2=[2,4,6,"diesel"]
print(len(mylst1))
mylt2[0]="benzin"
mylt2.append("lpg")# eisagvgh neou stoileiou
print(mylt2)
print(mylt2.pop()) #eksagwgh teleutaiou stoixeiou--> dinatothta print
mylt2.pop(0)
print(mylt2)


mylst3=[2,4,3,1,7]
#mylst3.sort() #taksinomisi listas
mylst3.reverse()
print(mylst3)

#lets try to print the elements in reverse
lst3=[1,2,3,4,5,6,7,8,9]

#for num in reversed(lst3):
for num in range(len(lst3),0,-1):
    print (num,end=" /")
print()


#add
a=[1,2,3,4,5]
a+=[6,7,8,]
print(a)