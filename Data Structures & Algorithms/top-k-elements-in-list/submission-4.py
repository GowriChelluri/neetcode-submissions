from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        res=[]
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True) 
        for key,value in sorted_freq[:k]:
            res.append(key)
        return res            
        