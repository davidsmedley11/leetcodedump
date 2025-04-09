class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        for x in nums1:
            nums3.append(x)
        for y in nums2:
            nums3.append(y)
        nums3.sort()
        n = len(nums3)
        median_position = int((n + 1) / 2)
        if len(nums3) % 2 == 1:
            median = nums3[median_position - 1]
        elif len(nums3) % 2 == 0:
            median = (nums3[median_position]  + (nums3[int((n / 2) - 1)])) / 2
        return median