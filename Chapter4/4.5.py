multiple_3 = list(range(3,31,3))
for number in multiple_3:
    print(number)
    
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)