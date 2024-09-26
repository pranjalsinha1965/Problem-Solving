def gencubes(n):
    for num in range(n):
        yield num**3 

for x in gencubes(10):
    print(x)
    