from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for num in nums:
            if m[num]:
                return True
            m[num]+=1
        return False

s = Solution()
answer = s.containsDuplicate([2,2,1,3])
print(answer)