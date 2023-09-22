
def counts(sentences):
    counts = []
    for i in sentences:
        counts.append(i.count(" "))
        return max(counts)+1
    
print(counts(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))