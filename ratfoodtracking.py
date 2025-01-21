r = int(input("Enter the no: of rats: "))
unit = int(input("Enter the unit of food: "))
m = int(input("Enter the no: of houses: "))
arr = [0] * m
for i in range(m):
    arr[i] = int(input("Enter the unit of food in house: "))

o = r * unit
k = 0
sum = 0
for i in range(m):
    if sum < o:
        sum = sum + arr[i]
        k += 1
    else:
        break

print(k)