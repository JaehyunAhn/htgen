# This is script to test KoNLPy.
# Project started at 01/18/2016. Author by Jaehyun Ahn(jaehyunahn@soagnag.ac.kr)
__author__ = 'Sogo'

from konlpy.tag import Kkma

print('Number of lines in document:')
k = Kkma()
f = open('test.txt', 'r')
lines = f.read().splitlines()
nlines = len(lines)
print(nlines)

sent = [k.sentences(lines[i]) for i in range(0, nlines)]

print('len <= 30 Sentences were:')
for i in range(len(sent)):
    for j in range(len(sent[i])):
        if(len(sent[i][j]) <= 30):
            print(sent[i][j])