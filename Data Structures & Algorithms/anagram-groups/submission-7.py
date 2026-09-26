class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            curr = [0] * 26
            for char in s:
                curr[ord(char) - ord('a')] += 1
            anagrams[tuple(curr)].append(s)
            
        
        return list(anagrams.values())

