from collections import Counter
def is_anagram(w1,w2):
    return Counter(w1) == Counter(w2)
s1="silent"
s2="listen"


print(is_anagram(s1,s2))