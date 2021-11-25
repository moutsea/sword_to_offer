import random
import time

def get_random_int(a=0, b=1e7, seed=None):
    if seed is not None:
        random.seed(seed)
    else:
        t = time.time()
        random.seed(t)
    return random.randint(a, b)


def get_random_list(n, a=0, b=1e7, seed=None):
    return [get_random_int(a, b, seed) for _ in range(n)]
