class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
                continue
            if A[j] % 2 == 1:
                j -= 1
                continue
            A[i], A[j] = A[j], A[i]

        return A