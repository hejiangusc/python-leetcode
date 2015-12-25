class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
    	dict = {}
    	for i in range(0, len(nums)):
    		if (target - nums[i]) in dict:
    			return [dict[target - nums[i]]+1, i+1]
    		dict[nums[i]] = i

test1 = Solution()
num_test1 = [1,2,6,22,34]
print test1.twoSum(num_test1, 8)

test2 = Solution()
num_test2 = [2,7,11,15]
print test2.twoSum(num_test2, 9)

test3 = Solution()
num_test3 = [1,3,5,6,8,23,45,56,34,22,46,102,114,7]
print test3.twoSum(num_test3, 78)

