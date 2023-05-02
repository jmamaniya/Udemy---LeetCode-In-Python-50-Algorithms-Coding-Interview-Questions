from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = n*(n+1)/2

        return int(intendedSum-currentSum)


s = Solution()
answer = s.missingNumber([9,6,4,2,3,5,7,0,1])
print(answer)
