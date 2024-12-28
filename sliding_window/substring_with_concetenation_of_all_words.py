'''
Need to extract all words from each window in s
If it is the same combination as words, all good
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        word_length = len(words[0])
        total_words = len(words)
        substring_length = word_length * total_words

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for i in range(len(s) - substring_length + 1):
            j = 0
            seen = {}

            while j < total_words:
                word_start = i + j * word_length
                word = s[word_start : word_start + word_length]

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1

                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            
            if j == total_words:
                res.append(i)
        
        return res