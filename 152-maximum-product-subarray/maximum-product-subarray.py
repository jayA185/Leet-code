class Solution:
    def maxProduct(self, nums):
        currentMax = nums[0]
        currentMin = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                currentMax, currentMin = currentMin, currentMax

            currentMax = max(num, currentMax * num)
            currentMin = min(num, currentMin * num)

            answer = max(answer, currentMax)

        return answer