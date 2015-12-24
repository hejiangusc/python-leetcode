class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
    	dict = {}
    	for i in range(0, len(nums)):
    		if (target - nums[i]) in dict:
    			return [dict[target - nums[i]]+1, i+1]
    		dict[nums[i]] = i

test1 = Solution()
num_test = [1,2,6,22,34]
print test1.twoSum(num_test, 8)

test2 = Solution()
num_test2 = [2,7,11,15]
print test2.twoSum(num_test2, 9)