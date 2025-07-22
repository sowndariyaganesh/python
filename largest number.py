arr = [5, 12, 7, 25, 3]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest number is:", largest)
