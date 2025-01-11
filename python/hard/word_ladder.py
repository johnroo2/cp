from collections import deque
from typing import List

#BAD SOLUTION

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        def steppable(w1, w2):
            return sum(1 for a, b in zip(w1, w2) if a != b) == 1

        queue = deque([(beginWord, 1)])

        while queue:
            current, steps = queue.popleft()
            to_remove = []
            for word in words:
                if steppable(current, word):
                    if word == endWord:
                        return steps + 1
                    queue.append((word, steps + 1))
                    to_remove.append(word)
            for word in to_remove:
                words.remove(word)

        return 0
