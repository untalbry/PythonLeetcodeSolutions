class Solution:
    def isAnagram(sef, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        s = sorted(s)
        t = sorted(t)
        print(s)
        print(t)
        return s == t

def main():
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))
if __name__ == "__main__":
    main()