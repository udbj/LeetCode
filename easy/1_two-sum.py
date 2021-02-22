class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx1 = 0
        idx2 = 0
        
        nums_dict = {}
        
        for idx,num in enumerate(nums):
            nums_dict[num] = idx
        
        for idx, num in enumerate(nums):
            req_num = target - num
            if req_num in nums_dict and nums_dict[req_num] is not idx:
                idx1 = idx
                idx2 = nums_dict[req_num]
        
        return [idx1, idx2]
