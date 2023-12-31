class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        ans = 1        # 一開始的答案是正的
        for n in nums: # 一序曲 n 出來
            ans *= n   # 答案 乘 n

        if ans>0: return 1
        if ans<0: return -1
        if ans==0: return 0