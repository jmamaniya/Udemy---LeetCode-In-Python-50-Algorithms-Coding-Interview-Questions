from typing import List


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    first_bad_version=3
    return version>=3

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while(left < right):
            mid = left+(right-left)//2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left

s = Solution()
answer = s.firstBadVersion(10)
print(answer)
