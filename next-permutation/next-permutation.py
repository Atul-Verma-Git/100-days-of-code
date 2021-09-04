class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in reversed(range(1,len(nums))):
            if nums[i-1] < nums[i]:
                x = nums[i-1]
                j = i
                m = 101
                while j < len(nums):
                    if nums[j] < m and nums[j] > x:
                        m = nums[j]
                        index = j    
                    j += 1
                nums[i-1], nums[index] = nums[index], nums[i-1]
                x = i
                while x < len(nums):
                    m = nums[x]
                    for _ in range(x,len(nums)):
                        if nums[_] <= m:
                            m = nums[_]
                            index = _ 
                    nums[x], nums[index] = nums[index], nums[x]
                    x += 1
                flag = 1
                break
        if flag == 0:
            nums.sort()
        