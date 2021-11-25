import random
from generate import Generate, Case
import numpy as np


class Case3(Case):
    def __init__(self):
        n, m = random.randint(1, 100), random.randint(1, 100)
        nums = sorted([random.randint(0, 100000000) for _ in range(n * m)])
        arr = np.array(nums).reshape((n, m))
        ans, k = 0, 0
        if random.randint(0, 100) > 50:
            ans = 1
            x, y = random.randint(0, n-1), random.randint(0, m-1)
            k = arr[x, y]
        else:
            while True:
                k = random.randint(0, 100000000)
                if k not in nums:
                    break
        self.n, self.m, self.k, self.ans = n, m, k, ans
        self.arr = arr

    def output(self, path, result_path, idx):
        with open(path, 'a+') as f:
            f.write('{} {} {}\n'.format(self.n, self.m, self.k))
            for i in range(self.n):
                for j in range(self.m):
                    f.write('{} '.format(self.arr[i, j]))
                f.write('\n')

        with open(result_path, 'a+') as f:
            f.write('case :{}\n'.format(idx + 1))
            f.write(str(self.ans))
            f.write('\n')


if __name__ == "__main__":
    generate = Generate(100, 3, Case3)
    generate.generate()
    generate.output()
