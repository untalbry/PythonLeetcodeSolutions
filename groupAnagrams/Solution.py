class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return strs
        anagrams = {}
        for str in strs:
            key = tuple(sorted(str))
            if key in anagrams:
                anagrams[key].append(str)
            else:
                anagrams[key] = [str]
        return list(anagrams.values())
        

def main():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs))

if __name__ == "main":
    main()
        