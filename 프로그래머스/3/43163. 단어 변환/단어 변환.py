from collections import deque, defaultdict
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    n = len(begin)
    word_dict = defaultdict(set)
    
    for word in [begin] + words:
        for word_ in words:
            if word != word_ and can_transform(word, word_):
                word_dict[word].add(word_)
                word_dict[word_].add(word)
    
    #print(word_dict)
    
    visited = {word:False for word in words+[begin]}
    
    return dfs(begin, target, word_dict, visited)

def can_transform(word_from, word_to):
    n = len(word_from)
    diff = 0
    for i in range(n):
        if word_from[i] != word_to[i]:
            diff += 1
        
        if diff > 1:
            return False
    
    return True
    

def dfs(word, target, word_dict, visited):
    result = 100
    if word == target:
        return 0
    if visited[word]:
        return result
    
    #print(word)
    trans_words = word_dict[word]
    #print(trans_words)
    visited[word] = True

    for trans_word in trans_words:
        if not visited[trans_word]:
            #print(word, trans_word)
            result = min(result, dfs(trans_word, target, word_dict, visited) + 1)
    
    return result