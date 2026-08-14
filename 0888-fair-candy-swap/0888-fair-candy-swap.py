class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        delta = (sumB - sumA) // 2
        setB = set(bobSizes)
        
        for x in aliceSizes:
            if x + delta in setB:
                return [x, x + delta] 