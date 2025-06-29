## return the lenght of the longest substring without duplicate characters

def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    longest = 0
    n = len(s)
    sett = set()

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        sett.add(s[r])
        w = (r-l) + 1
        longest = max(w, longest)
    return longest

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('aaaaaaaaaaaaaaaaa'))

