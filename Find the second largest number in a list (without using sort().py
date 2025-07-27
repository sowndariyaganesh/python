numbers = [12, 45, 2, 41, 31, 10]

largest = -1
second = -1

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number is:", second)
