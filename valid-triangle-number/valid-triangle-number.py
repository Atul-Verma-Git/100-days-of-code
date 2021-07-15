class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def bini(arr,num):
            first = 0
            last = len(arr)-1
            while True:
                mid = (first + last) // 2
                if last == first:
                    if arr[mid] < num:
                        return last + 1
                    return last
                if arr[mid] >= num:
                    last = mid
                elif arr[mid] < num:
                    first = mid + 1

        nums.sort()
        count = 0
        d = {}
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i]+nums[j] not in d.keys():
                    d[nums[i]+nums[j]] = bini(nums,nums[i]+nums[j])
                    count += max(d[nums[i]+nums[j]] - j -1, 0)
                else:
                    count += max(d[nums[i]+nums[j]] - j -1,0)
                    
                
        return count
        