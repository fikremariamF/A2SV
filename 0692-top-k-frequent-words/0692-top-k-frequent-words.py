class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        print(count)
        counts = set()
        wordsPerCount = defaultdict(set)
        
        for key in count:
            wordsPerCount[count[key]].add(key)
            counts.add(count[key])
        
        output = []
        
        counts = list(map(lambda x: -1 * x, counts))
        heapify(counts)
        
        while len(output) < k:
            key = heappop(counts)
            
            words = list(wordsPerCount[key * -1])
            words.sort()
            output.extend(words)
        
        return output[:k]