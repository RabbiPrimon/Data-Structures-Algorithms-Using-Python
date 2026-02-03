class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        # Phase 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False  # no increasing part

        # Phase 2: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == n - 1:
            return False  # no final increasing part

        # Phase 3: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
