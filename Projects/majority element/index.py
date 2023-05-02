from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        for num in nums:
            if m[num] > len(nums) // 2:
                return num


s = Solution()
answer = s.majorityElement([2, 2, 2, 2, 1, 3])
print(answer)
