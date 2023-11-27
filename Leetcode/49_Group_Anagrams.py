# Group Anagrams 

"""Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# Ways of grouping anagrams: 
## sort-> n(log n) time complexity
## reverse 

"""
Using a hashmap
eat = 1e, 1a, 1t
tea = 1e, 1a, 1t
ate = 1e, 1a, 1t
key:[eat,tea]

O(m) where m is the total number of strings
O(n) where n is the count of alphabets in the string
count =  26 (lowercase alphabets)
So, time complexity = O(m*n*26)-> 0(m*n)
"""

class Solution: 
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdic(list) # mapping charCount to list of Anagrams 

    for s in strs:
      count = [0] * 26 # a ... z 

      for c in s:
        count[ord(c) - ord("a")] +=1

      res[tuple(count)].append(s)
    return res.values()
        # ASCII values 
          # a = 80 -> 0, 80-80
          # b = 81 -> 1, 81-80

## Another way 
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
