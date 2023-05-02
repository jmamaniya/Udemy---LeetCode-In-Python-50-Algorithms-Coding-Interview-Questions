from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            if (goal in m):
                return [m[goal], i]
            m[nums[i]] = i

s = Solution()
answer = s.twoSum([3,3,2,2,1],4)
print(answer)

