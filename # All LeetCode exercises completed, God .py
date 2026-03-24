# All LeetCode exercises completed, God help us all 
""" Q1: Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays. Return the array ans."""
def concatenation(nums: list[int]): 
    nums2 = []
    for num in nums: 
        nums2.append(num)
    listy = nums + nums2 
    return listy 
""" 
print(concatenation([1, 2, 3])) 
print(concatenation([1, 3, 2, 1])) 
"Beats 100% runtime, 68% memory, I wonder how different data structures would contribute to memory usage"
"""


"""Q2: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]
Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""
def shuffle(nums:list[int], n:int): 
    listy = []
    xlist = [nums[i] for i in range(0, n)]
    ylist = [nums[i] for i in range(n, len(nums))] 
    for i in range(len(xlist)): 
        listy.append(xlist[i])
        listy.append(ylist[i]) 
    return listy 
""" 
print(shuffle([2,5,1,3,4,7], 3))
print(shuffle([1,2,3,4,4,3,2,1], 4))
print(shuffle([1, 1, 2, 2], 2)) 
"beats 81% runtime wise and 40% memory wise, I think runtime is O(N) how would you reduce that?"
"""

def maxConsecutiveOnes(listy: list[int]): 
    map = {}
    for num in listy: 
        if num in map.keys(): 
            map[num] += 1 
        map[num] = 0 
""" 
print(maxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
"""

def find_the_difference(s: str, t: str):
    s_map = {}
    t_map = {}
    if s == "": 
        return t 
    
    for char in s: 
       s_map[char] = s_map.get(char, 0) + 1 # creating a key with a value and then incrementing by 1 if that key already exists in the dictionary

    for char in t: 
        t_map[char] = t_map.get(char, 0) + 1 

    for char in t_map.keys(): 
        if char not in s_map.keys() or t_map[char] != s_map[char]: 
            return char
""" 
print(find_the_difference("abcd", "abcde"))
print(find_the_difference("", "y")) 
print(find_the_difference("a", "aa"))
print(find_the_difference("abbcd", "acdbbe"))
"""

def strStr(haystack: str, needle: str): 
    stringy = ""
    for i in range(len(haystack)): 
        stringy += haystack[i] 
        if stringy == needle: 
            return len(stringy) - (i + 1)
    return -1 

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("foodiebyfoot", "by"))




