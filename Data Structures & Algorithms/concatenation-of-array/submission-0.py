class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [None]*size*2
        for i, n in enumerate(nums):
            result[i] = nums[i]
            if(i == 0):
                result[size] = nums[i]
            else:
                result[i+size] = nums[i]
        return result