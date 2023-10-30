from time import time
from random import randint
from random import choice

def quick_sort(ls:list)->list:
    if len(ls) <= 1:
        return ls
    pvt = choice(ls)
    left = [i for i in ls if i < pvt] 
    center = [i for i in ls if i == pvt]
    right = [i for i in ls if i > pvt]
    return quick_sort(left) + center + quick_sort(right)

if __name__ == "__main__":
    n = 1000
    ls = [randint(-100,100) for i in range(n)]
    start = time()
    ls = quick_sort(ls)
    print(time()-start)