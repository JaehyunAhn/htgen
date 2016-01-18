# This is script to test KoNLPy.
# Project started at 01/18/2016. Author by Jaehyun Ahn(jaehyunahn@soagnag.ac.kr)
__author__ = 'Sogo'

# To parallel processing
from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from threading import Thread
import jpype

def do_concurrent_tagging(start, end, lines, result):
    jpype.attachThreadToJVM()
    l = [k.sentences(lines[i]) for i in range(start, end)]
    result.append(l)
    l = [k.nouns(lines[i]) for i in range(start, end)]
    result.append(l)
    return

if __name__ == "__main__":
    import time

    # Read Docs
    print('Number of lines in document:')
    k = Kkma()
    f = open('test.txt', 'r')
    lines = f.read().splitlines()
    nlines = len(lines)
    print(nlines)

    # Print Docs
    print('Concurrent Tagging:')
    t0 = time.time()
    result = []
    t1 = Thread(target=do_concurrent_tagging, args=(0, int(nlines/4), lines, result))
    t2 = Thread(target=do_concurrent_tagging, args=(int(nlines/4), int(nlines*2/4), lines, result))
    t3 = Thread(target=do_concurrent_tagging, args=(int(nlines*2/4), int(nlines*3/4), lines, result))
    t4 = Thread(target=do_concurrent_tagging, args=(int(nlines*3/4), nlines, lines, result))
    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join(); t2.join(); t3.join(); t4.join()

    # Print Time: T
    m = sum(result, [])
    print(time.time() - t0)
    f.close()
    print(m)