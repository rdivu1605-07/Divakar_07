class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = [0] * 26
        total = 0
        
        for ch in s:
            idx = ord(ch) - ord('a')
            new_for_ch = (total + 1) % MOD
             
            total = (total - ends_with[idx] + new_for_ch) % MOD
            ends_with[idx] = new_for_ch
            
        return total 