# Author: Nguyen L.
# Date: May 20th, 2020
# Return the number of even ints in the given array.

import random

def countEvens(nums):

    count = 0

    for i in nums:
        if i % 2 == 0:
            count += 1

    return count

randomList = []

for i in range(0, 5):
    num = random.randint(1, 50)
    randomList.append(num)

print("List of numbers: ", end='')
print(randomList)
print("Count evens: " + str(countEvens(randomList)))

