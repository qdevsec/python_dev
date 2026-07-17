# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# anagram: t is made up of all the characters in s

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # lengths need to be the same so check first
        if len(s) != len(t):
            return False
        
        # creating hash map that will have char as index and count as value
        count_of_s, count_of_t = {}, {} 

        # loop through range of length of word
        for i in range(len(s)):
            # create keys from chars, update count
            # use hashmap function get() so that if the key doesnt exist
            # the default value is the function will return is 0 so missing
            # key error doesn't get thrown
            count_of_s[s[i]] = 1 + count_of_s.get(s[i], 0)
            count_of_t[t[i]] = 1 + count_of_t.get(t[i], 0)

        # loop through hashmaps and make sure the values for the keys
        for a in count_of_s:
            if count_of_s[a] != count_of_t.get(a, 0):
                return False
        
        return True

