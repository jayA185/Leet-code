class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            new_subsets = []

            for subset in result:
                new_subsets.append(subset + [num])

            result.extend(new_subsets)

        return result   