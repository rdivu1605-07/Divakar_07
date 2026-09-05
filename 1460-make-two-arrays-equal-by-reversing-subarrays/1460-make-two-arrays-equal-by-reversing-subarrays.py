class Solution:
    def canBeEqual(self, targetArray: List[int], currentArray: List[int]) -> bool:
        elementCounts = [0] * 1001
        uniqueCount = 0
        
        for t, c in zip(targetArray, currentArray):
            if elementCounts[t] == 0:
                uniqueCount += 1
            elementCounts[t] += 1
            
            if elementCounts[c] == 1:
                uniqueCount -= 1
            elementCounts[c] -= 1
        
        return uniqueCount == 0 