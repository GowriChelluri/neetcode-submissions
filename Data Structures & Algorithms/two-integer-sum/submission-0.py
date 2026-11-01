class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,value in enumerate(nums):
            complement=target-nums[i]
            if complement in freq:
                return [freq[complement],i]
            freq[value]=i    

        