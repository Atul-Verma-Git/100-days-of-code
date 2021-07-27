class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def search(arr, start, end, num):
            if arr[end] <= num:
                return end + 1
            if arr[start] >= num:
                return start
            mid = (start + end+1) // 2
            if ((mid - 1 < 0 or arr[mid-1] < num) and arr[mid] > num) or arr[mid] == num:
                return mid
            elif arr[mid] > num:
                return search(arr, start, mid , num)
            elif arr[mid] < num:
                return search(arr, mid , end, num)
        
        j = 0
        for i in nums2:
            j = search(nums1, j, m-1, i)
            print(j)
            m += 1
            for x in reversed(range(j+1, m)):
                nums1[x] = nums1[x-1]
            nums1[j] = i
        
            
            
            
        