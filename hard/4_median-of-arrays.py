class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = 0
        j = 0
        
        x = []
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        while i<len1 and j<len2:
            while i < len1 and nums1[i] <= nums2[j]:
                x.append(nums1[i])
                i = i + 1
            if not i < len1:
                break
            while j < len2 and nums2[j] < nums1[i]:
                x.append(nums2[j])
                j = j + 1

        
        while i < len1:
            x.append(nums1[i])
            i = i + 1
        
        while j < len2:
            x.append(nums2[j])
            j = j + 1
        
        xlen = len(x)
        
        if xlen % 2 is 0:
            median = (x[xlen//2] + x[xlen//2 - 1])/2
        else:
            median = x[xlen//2]
            
        return median
