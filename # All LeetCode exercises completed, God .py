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
    front = 0
    back = len(needle)

    curr = haystack[front:back]
    
    while curr != needle and front < len(haystack): 
        front += 1 
        back += 1 
        curr = haystack[front:back]
    
    if front == len(haystack): 
        return -1 
    
    else: 
        return front        


def isAnagram(s: str, t:str): 
   s_map = {}
   t_map = {} 

   if len(s) != len(t): 
       return False
   
   for char in s: 
       s_map[char] = s_map.get(char, 0) + 1 
    
   for char in t:
       t_map[char] = t_map.get(char, 0) + 1 
   
   if s_map.keys() != t_map.keys(): 
       return False 
   
   else: 
       for char in s_map.keys(): 
          if s_map[char] != t_map[char]: 
              return False     
   
   return True 


def repeatedSubstringPattern(s: str): 
   # length of substring is at most half of length of parent string, remainder has to be 0 
   valid_lengths = []

   for i in range(1, len(s)): 
       if i <= len(s) // 2 and len(s) % i == 0: # all valid lengths will be half the length of s with no remainder 
           valid_lengths.append(i) 

   for length in valid_lengths: # length = [1, 2]
       substring = s[:length] # all substrings must begin at the start of s 
       repeat = len(s) // len(substring) # you only need to repeat a certain number of times to determine if the substring is a valid one
       substring *= repeat 
       if substring == s: 
           return True 
   return False 
 
"""Filtering through lengths by finding only the valid ones 
Figuring out how many times you need to repeat
Filtering through valid lengths to find the correct word """

def moveZeros(nums): 
    pointer = 0
    for i in range(len(nums)): 
        if nums[i] != 0: 
            nums[pointer] = nums[i]
            pointer += 1 
    
    for x in range(pointer, len(nums)): 
        nums[x] = 0 
    
    return nums

""" Trying to iterate through the list and change items as you go doesn't work 
instead have one pointer that iterates through the list, 
and one pointer that changes the item it's supposed to; 
it doesn't move until there's something change; once you've pushed everything forward, 
all you have to do is go back and set the rest of the list to 0 """


def plusOne(digits): 
    num = "" 
    for digit in digits: 
        new_digit = str(digit)
        num += new_digit 

    num = int(num)
    num += 1 
    num = str(num)
    listy = []
    for char in num: 
        char = int(char)
        listy.append(char)
    
    digits = listy 

    return digits 



def arraySign(nums):
    total = 1
    for num in nums: 
        total *= num 
    
    def signFunc(x): 
        if total > 0: 
            return 1 
        elif total == 0: 
            return 0 
        else: 
            return -1 
    
    return signFunc(total)



# there's a bunch of sorting algorithms you could probably do for this 
def canMakeArithmeticProgression(arr): 
    arr.sort()
    diff = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1): 
        if abs(arr[i] - arr[i + 1]) != diff: 
            return False 
    return True 

""" checking consecutive groups means you can just iterate through groups in the list 
and compare to an initial value or whatever you don't have to take chunks and compare within one iteration
it doesn't work you run into out of range index errors """


""" An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise."""

def ascending(nums): 
    for i in range(len(nums) - 1): 
        if nums[i] > nums[i + 1]: 
            return False 
    return True

def descending(nums): 
    for i in range(len(nums) - 1): 
        if nums[i] < nums[i + 1]: 
            return False 
    return True 

def isMonotonic(nums: list): 
   if not ascending(nums) and not descending(nums): 
       return False 
   return True  
   
def toRomanInt(s): 
    romanRef = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    total = 0

    reversed_s = s[::-1]

    prev = 0 
    for i in range(len(reversed_s)): 
        if romanRef[reversed_s[i]] < prev: 
            total -= romanRef[reversed_s[i]]
        else: 
            total += romanRef[reversed_s[i]]

        prev = romanRef[reversed_s[i]]
    return total 

""" To solve this problem the main thing is the iteration. Reversing the list and running through it backwards ensures that you'll see the larger
value first; from there all you have to do is subtract the smaller value from the total since you already added the larger value to total during other parts
of the iteration; if this case isn't needed then just add the value to the total like normal; the prev value is to keep track of who you saw before in order to make the comparison
needed for the first conditional statement; prev is not needed if you decide to iterate normally and compare the current element with the element in front of it"""


def lengthofLastWord(s): 
    new_s = s.split()
    return len(new_s[-1])
""" split function gets rid of spaces and puts each individual word in a list"""


def toLowerCase(s): 
    return s.lower()


def calPoints(operations): 
    score = []
    for op in operations: 
        if op == "+": 
            score1 = score[-1]
            score2 = score[-2]
            score.append(score1 + score2)
        elif op == "D": 
            score1 = score[-1] * 2 
            score.append(score1)
        elif op == "C": 
            score.pop(-1)
        else: 
            op = int(op)
            score.append(op)

    return sum(score)
""" The score changing is dependent on identifying what the most recent score was; using a stack data structure is the natural approach for this problem because 
stacks identify who the first item and most previous item added was by default; this makes it incredibly easy to change the score depending on the operation"""


def judgeCircle(moves): 
    return False 


