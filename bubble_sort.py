def bubble_sort(nums):
    loop1 = 0
    swaps = 0
    loop2 = 0
    for x in range (len(nums)-1):
        loop1 += 1
        #inner loop
        for y in range (len(nums)-x-1):
            loop2 += 1
            #check right value of each index for swap
            if nums[y] > nums[y + 1]:
                swaps += 1
                temp = nums[y]
                nums[y] = nums[y + 1]
                nums[y + 1] = temp
    print("Sorted: " , nums , "\n")
    print("\nLoops: " , loop1 + loop2 , " \nSwaps: " , swaps)
