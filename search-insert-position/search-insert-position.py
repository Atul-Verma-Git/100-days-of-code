class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
                    
        return bini(nums, target)