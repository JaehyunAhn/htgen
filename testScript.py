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
    l = [k.pos(lines[i]) for i in range(start, end)]
    result.append(l)
    return

if __name__ == "__main__":
    import time

    # Read Docs
    print('Number of lines in document:')
    k = Kkma()
    lines = kolaw.open('constitution.txt').read().splitlines()
    nlines = len(lines)
    print(nlines)

    # Print Docs
    print('Concurrent Tagging:')
    t0 = time.time()
    result = []
    t1 = Thread(target=do_concurrent_tagging, args=(0, int(nlines/2), lines, result))
    t2 = Thread(target=do_concurrent_tagging, args=(int(nlines/2), nlines, lines, result))
    t1.start(); t2.start()
    t1.join(); t2.join()

    # Print Time: T
    m = sum(result, [])
    print(time.time() - t0)
    print(m)