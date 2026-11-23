class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, n in enumerate(nums):
            if(hashmap.get(n) is not None):
                return [hashmap[n], idx]
            hashmap[target-n] = idx
        return []