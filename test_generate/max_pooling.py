from generate import Generate, Case
import random_tool

class CaseMaxPooling(Generate):
    def __init__(self):
        n = random_tool.get_random_int(10, 1000)
        k = random_tool.get_random_int(1, n-1)
        nums = random_tool.get_random_list(n)
        self.n = n
        self.k = k
        self.arr = nums
        self.pooling = []
        for i in range(0, n-k+1):
            self.pooling.append(max(nums[i: i+k]))

    def output(self, path, result_path, idx):
        with open(path, 'a+') as f:
            f.write('{} {}\n'.format(self.n, self.k))
            for i in range(self.n):
                f.write('{} '.format(self.arr[i]))
            f.write('\n')

        with open(result_path, 'a+') as f:
            f.write('case :{}\n'.format(idx + 1))
            for i in self.pooling:
                f.write('{} '.format(i))
            f.write('\n')


if __name__ == '__main__':
    generate = Generate(100, 'max_pooling', CaseMaxPooling)
    generate.generate()
    generate.output()