class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxi = (1<<maximumBit) - 1
        xor = 0
        output = []
        for i in nums:
            xor ^= i
            output.append(maxi ^ xor)
        print(output)
        return reversed(output)
        