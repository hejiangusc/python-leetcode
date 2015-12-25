class Solution:
    # @return a tuple, (index1, index2)
    def lengthOfLongestSubstring(self, s):
    	if s == None or len(s) == 0:
    		return 0
    	dict = set()
    	leftBound = 0
    	maxNum = 0
    	for i in range(0, len(s)):
            if s[i] in dict:
            	while leftBound < i and s[leftBound] != s[i]:
            		dict.discard(s[leftBound]) 
            		leftBound += 1
                leftBound += 1
            else:
            	dict.add(s[i])
            	maxNum = max(maxNum, i - leftBound + 1)
        return maxNum

################# test case 1 ###################
test1 = Solution()
str = "abcabcbb"
print test1.lengthOfLongestSubstring(str)

################# test case 2 ###################
test2 = Solution()
str = "abcabcbbeudskdf"
print test2.lengthOfLongestSubstring(str)