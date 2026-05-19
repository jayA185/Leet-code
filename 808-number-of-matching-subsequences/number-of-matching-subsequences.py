from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words):
        buckets = defaultdict(list)
        
        # put words in bucket of first character
        for word in words:
            buckets[word[0]].append(word)
        
        count = 0
        
        for char in s:
            waiting_words = buckets[char]
            buckets[char] = []
            
            for word in waiting_words:
                if len(word) == 1:
                    count += 1
                else:
                    buckets[word[1]].append(word[1:])
        
        return count