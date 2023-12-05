import re

# input = open("input.txt", "r")
# content = input.readlines()

with open("input.txt", "r") as file:
    total = 0

    for line in file.read().splitlines():
        nums = []

        for i in line:
            if i.isdigit():
                nums.append(i)
                print(nums)
        
        score = int(nums[0] + nums[-1])
        total += score

    print(total)
