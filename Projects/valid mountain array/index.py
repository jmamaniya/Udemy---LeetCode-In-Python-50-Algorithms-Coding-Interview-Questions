from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if (len(A) < 3):
            return False

        i = 1
        while (i < len(A) and A[i] > A[i - 1]):
            i += 1

        if (i == 1 or i == len(A)):
            return False

        while (i < len(A) and A[i] < A[i - 1]):
            i += 1

        return i == len(A)


s= Solution()
answer = s.validMountainArray([0,3,2,1])
print(answer)