# This is script to test KoNLPy.
# Project started at 01/18/2016. Author by Jaehyun Ahn(jaehyunahn@soagnag.ac.kr)
__author__ = 'Sogo'

from konlpy.tag import Kkma
from collections import Counter

print('Number of lines in document:')
k = Kkma()
f = open('test.txt', 'r')
lines = f.read().splitlines()
nlines = len(lines)
print(nlines)

nouns = [k.nouns(lines[i]) for i in range(0, nlines)]

cnt = Counter()
for i in range(len(nouns)):
    for j in range(len(nouns[i])):
        cnt[nouns[i][j]] += 1
print(cnt.most_common(15))
# let's get words! It's a steal!
print(cnt.most_common(15)[0][0])
print(cnt.most_common(15)[1])