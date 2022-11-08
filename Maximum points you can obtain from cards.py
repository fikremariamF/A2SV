class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        total= sum(cardPoints)
        
        window_size = n - k
        max_score = 0
        M
        windowSum = sum(cardPoints[:window_size])
        
        i = 0
        while i + window_size <= n:
            if i > 0:
                windowSum -= cardPoints[i-1]
                windowSum += cardPoints[i+window_size-1]
            max_score = max(max_score, total - windowSum)
            i += 1
        
        return max_score
