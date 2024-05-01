from collections import defaultdict, deque

def solution(begin, target, words):
    
    n = len(words)
    if target not in words:
        return 0
    
    visited = {word: False for word in words}
    
    result = dfs(begin, target, words, visited, count=0)
    
    return result

def dfs(begin, target, words, visited, count):
    n = len(words)
    
    result = n+1
    for i, word in enumerate(words):
        if not visited[word] and can_transform(begin, word):
            if word == target:
                return count + 1
            else :
                visited[word] = True
                result = min(result, dfs(word, target, words, visited, count+1))
                visited[word] = False
    
    return result if result != n+1 else 0
            
def can_transform(word1, word2):
    n = len(word1)
        
    count = 0
    for i in range(n):
        if word1[i] != word2[i]:
            count +=1
        if count > 2:
            return False
    
    return True if count == 1 else False
    