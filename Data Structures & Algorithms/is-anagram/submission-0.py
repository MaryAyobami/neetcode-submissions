class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s);
        t_array = list(t)
        if len(s_array) != len(t_array):
            return False
        else:
            frequencies = {};
            for item in s_array:
                frequencies[item] = frequencies.get(item, 0) + 1
            for item in t_array:
                if item in frequencies:
                    frequencies[item] -= 1
                else:
                    frequencies[item] = -1 

            is_anagram = all(count == 0 for count in frequencies.values())

            return is_anagram