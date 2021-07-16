class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        output = []
        for i in candies:
            if i + extraCandies >= maxi:
                output.append(True)
            else:
                output.append(False)
        return output