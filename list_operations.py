numbers = []                                            # create an empty list to store the numbers
for i in range(5):                                      # starts a for loop that runs 5 times, from 0 - 4
    value = int(input(f"Enter integer #{i + 1}: "))
    numbers.append(value)

print("Original list:", numbers)

sorted_version = sorted(numbers)
print("sorted version (original unchanged):", sorted_version)
print("Original list after sorting:", numbers)

numbers.sort()
print("original list after .sort():", numbers)

numbers.append(99)
print("Original list after appending 99:", numbers)

numbers.remove(99)
print("List after removing 99 by value:", numbers)

del numbers[0]
print("List after removing element at index 0:", numbers)

numbers.reverse()
print("List after reverse():", numbers)