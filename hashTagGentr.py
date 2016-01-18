# This is script to test KoNLPy.
# Project started at 01/18/2016. Author by Jaehyun Ahn(jaehyunahn@soagnag.ac.kr)
__author__ = 'Sogo'

from konlpy.tag import Kkma
from collections import Counter
from threading import Thread
import jpype

"""
Kkma Using Part: These codes took a huge time
"""
def do_concurrent_tagging(isNoun, start, end, lines, result):
    jpype.attachThreadToJVM()
    if (isNoun == True):
        # check nouns
        l = [k.nouns(lines[i]) for i in range(start, end)]
    else:
        # check sentences
        l = [k.sentences(lines[i]) for i in range(start, end)]
    result.append(l)
    return 0

"""
Main Module: Take apart, split nouns and sentences. Finally add up a hashtag
"""
if __name__ == "__main__":
    import time
    # Read Docs
    print('Number of lines in document:')
    k = Kkma()
    f = open('test.txt', 'r')
    lines = f.read().splitlines()
    nlines = len(lines)

    # Print Docs
    t0 = time.time()
    print('Concurrent Tagging:')
    nouns = []
    sentences = []
    # t1, t2 are for nouns / t2 and t4 are for sentences
    t1 = Thread(target=do_concurrent_tagging, args=(True, 0, int(nlines/2), lines, nouns))
    t2 = Thread(target=do_concurrent_tagging, args=(True, int(nlines/2), nlines, lines, nouns))
    t3 = Thread(target=do_concurrent_tagging, args=(False, 0, int(nlines/2), lines, sentences))
    t4 = Thread(target=do_concurrent_tagging, args=(False, int(nlines/2), nlines, lines, sentences))

    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join(); t2.join(); t3.join(); t4.join()

    # Print time: delta
    print(time.time() - t0)
    f.close()

    # Result processing
    m_nouns = sum(nouns, [])
    m_sentences = sum(sentences, [])
    print('Hashtags(#) will be:')
    # Hashtag for Nouns
    cnt = Counter()
    for i in range(len(m_nouns)):
        for j in range(len(m_nouns[i])):
            cnt[m_nouns[i][j]] += 1
    #print(cnt.most_common(15))
    for i in range(15):
        print('#' + cnt.most_common(15)[i][0])

    # Hashtag for Sentences <= 20
    for i in range(len(m_sentences)):
        for j in range(len(m_sentences[i])):
            if((len(m_sentences[i][j]) <= 20) & (len(m_sentences[i][j]) >= 2)):
                #print(m_sentences[i][j])
                # if user wants to _ or ' '(blank), then replace it!
                # replace(origin, replace, count)
                target_sentences = str(m_sentences[i][j]).replace(' ', '')
                target_sentences = target_sentences.replace('.', '')
                # target_sentences = target_sentences.replace('“','')
                # target_sentences = target_sentences.replace('”','')
                # target_sentences = target_sentences.replace("'",'')
                print('#' + target_sentences)