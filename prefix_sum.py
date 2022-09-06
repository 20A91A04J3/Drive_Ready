class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        dic={0:1}
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if(summ-k in dic.keys()):
                cnt+=dic[summ-k]
            dic[summ]=dic.get(summ,0)+1
        return cnt
            
