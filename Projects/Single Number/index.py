from typing import \
    List
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)

s = Solution()
answer = s.singleNumber([3,3,2,2,1])
print(answer)