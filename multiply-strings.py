class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs.sort(key=lambda given: "".join(sorted(given)))
        print(strs)


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
