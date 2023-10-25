class Solution:
    @cache
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
    
        prev_k = (k + 1) // 2
        prev_symbol = self.kthGrammar(n - 1, prev_k)

        if prev_symbol == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0