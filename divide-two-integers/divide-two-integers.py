class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if -1<<31 <= int(dividend/divisor) and (1<<31)-1 >= int(dividend/divisor):
            return int(dividend/divisor)
        return (1<<31) - 1
        