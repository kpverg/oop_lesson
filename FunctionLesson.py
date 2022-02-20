def my_function(name):
    print(f"hello {name}")


def addd_func(num1,num2):
    return num1+num2

def say_hallo(name="Random"):
    print(f"hello {name}")

def isEven(num):
    if num%2==0:
        print("is Even")
        return True
    else:
        print("is Odd")
        return False

def checkEven(numLst):
    evenLst=[]
    for num in numLst:
        if num%2==0:
            evenLst.append(num)
        else:
            pass
    return evenLst







if isEven(4): print("success")
my_function("Gus")
say_hallo("peter")
result=addd_func(3,4)
result=addd_func("3","4")
print(f"result is {result}")

print(checkEven([1,2,5,7,8,56]))