import os
output_path_base = '../test/data'
result_path_base = '../test/result'

class Case:
    def output(self, data_path, result_path, idx):
        raise NotImplementedError()


class Generate:
    def __init__(self, n, problem_id, Case):
        self.n = n
        self.problem_id = problem_id
        self.output_path = os.path.join(output_path_base, '{}.txt'.format(problem_id))
        self.result_path = os.path.join(result_path_base, '{}.txt'.format(problem_id))
        self.cases = []
        self.Case = Case

    def generate(self):
        # raise NotImplementedError()
        for _ in range(self.n):
            self.cases.append(self.Case())

    def output(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

        if os.path.exists(self.result_path):
            os.remove(self.result_path)

        f = open(self.output_path, 'w')
        f.write('{}\n'.format(self.n))
        f.close()

        for i in range(self.n):
            print('generating case{}ing'.format(i))
            self.cases[i].output(self.output_path, self.result_path, i)
        f.close()
# if __name__ == '__main__':
#     generate = Generate(100, 3)
#     print(generate.output_path)