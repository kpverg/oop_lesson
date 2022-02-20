def createCubes(n):
    
    for x in range(n):
        yield (x**3)


n=10
for i in createCubes(n):
    print(i)

print(list(createCubes(n)))