def selection_sort(nums):
    loop1 = 0
    swaps = 0
    loop2 = 0
    for x in range(len(nums)-1):
        loop1 += 1
        #current minimum index starts at 0
        min = x
        for y in range (x + 1 , len(nums)):
            loop2 += 1
            #if the right index is less than the min index, then swap
            if nums[y] < nums[min]:
                swaps += 1
                min = y
            nums[x] , nums[min] = nums[min] , nums[x]
    print("Sorted" , nums)
    print("\n Loops: " , loop1 + loop2 , "\n Swaps: " , swaps)
