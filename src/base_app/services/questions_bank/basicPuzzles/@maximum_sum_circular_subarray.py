class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        k1 = self.kadane_modified(nums) 
        cs = sum(nums)
        prime_a = [-item for item in nums]
        # for i in range(len()):
        #     cs += A[i]
        #     A[i] = -A[i]
        k2 = self.kadane_modified(prime_a)
        cs = cs + k2
        if cs > k1 and cs != 0:
            return cs
        return k1

    def kadane_modified(self, A:List[int]) -> int:
        sum_till_now = A[0]
        max_sum = A[0]
        for item in A[1:]:
            sum_till_now = max(item, sum_till_now + item)
            max_sum = max(sum_till_now, max_sum)
        return max_sum

    # def kadane(self, A:List[int]) -> int:
    #     sum_till_now = 0
    #     max_sum = 0
    #     for i, item in enumerate(A):
    #         sum_till_now += item
    #         if sum_till_now < 0:
    #             sum_till_now = 0
    #         max_sum = max(sum_till_now, max_sum)
    #     return max_sum