class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        result = []
        nums.sort()
        d = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in d.keys():
                    d[nums[i]+nums[j]] = [[i,j]]
                else:
                    d[nums[i]+nums[j]].append([i,j])        
        b = list(d.keys())
        final = {}
        output = []
        for i in range(len(b)):
            if target - b[i] in final.keys():
                output.append([final[target - b[i]], i])
            else:
                final[b[i]] = i
        if target % 2 == 0:
            output.append([final[target//2],final[target//2]])
        
        for i in range(len(output)):
            for j in d[b[output[i][0]]]: 
                for k in d[b[output[i][1]]]:
                    if len(set(k+j)) == 4:
                        result.append([k+j])
        return set(result)
    '''
    
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  
                return
            if N == 2: 
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: 
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

                             