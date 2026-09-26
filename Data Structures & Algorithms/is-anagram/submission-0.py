class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if chars.get(char) == None:
                chars[char] = 1
            else:
                chars[char] = chars[char] + 1
    
        
        for char in t:
            if chars.get(char) == None:
                return False
            else:
                chars[char] = chars[char] - 1
                if chars[char] == 0:
                    chars.pop(char)
        
        if not chars:
            return True
        else:
            return False        
