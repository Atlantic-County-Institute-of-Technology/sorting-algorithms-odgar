import random

def insertion_sort(nums):
    loop1 = 0
    swaps = 0
    #original numbers
    for x in range(len(nums)):
        loop1 += 1
        #key = the x index of nums
        key = nums[x]
        y = x - 1
        while y>= 0 and key < nums[y]:
            swaps += 1
            nums[y + 1] = nums[y]
            y -= 1
        nums[y + 1] = key
    #sorted numbers
    print("Sorted: " , nums)
    print("\n Loops: " , loop1, "\n Swaps: " , swaps)
