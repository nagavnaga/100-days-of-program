from collections import Counter
from collections import defaultdict

#Counter example to find out the most common word in a file




filename=r'C:\Users\venkan5\Desktop\desktop\config_naga.txt'

with open(filename) as fin:
    words = fin.read().split()
#with out Counter

common_words={}
for word in words:
    if word not in common_words:
        common_words[word]=0
    common_words[word]+=1

for word, reputition in sorted(common_words.items(),
                               key= lambda x:x[1],reverse=True)[:5]:
    print(word, reputition)

# one liner with counter :)

print(Counter(words).most_common(5))


'''
Deque 
'''