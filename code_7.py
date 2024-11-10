#printing numbers from 1-20

for i in range(1,20):
    print(i)

#printing numbers from 1-1 million

list = []

for i in range(1,1000000):
    print(i)

    list.append(i)

print(list)

print("Min of the list: ")
print(min(list))

print("Max of the list: ")
print(max(list))

print("Sum of the list: ")
print(sum(list))

#odd number
odd = []


for a in range(1,20):
    if (a % 2 != 0):
        odd.append(a)

print("Odd number: ")
print(odd)


#multiples of 3 

multi = []

for r in range(3,30,3):

    multi.append(r)

print("Multiple of 3: ")
print(multi)

#cubes

cubes = []

for i in range(1,10):
    cubes.append(i**3)

print("Cubes are: ")
print(cubes)

