import argparse
import sys
import os
import importlib

sys.path.append('./test_generate/')

parser = argparse.ArgumentParser()
parser.add_argument("-problem_id")
args = parser.parse_args()

source_path = './program'
test_path = './test/data'
answer_path_base = './test/result'

def delete_files(bin_path):
    os.system('rm -rf cur')
    os.system('rm -rf {}'.format(bin_path))

def get_cpp_result(code_path, bin_path, data_path, output_path):
    compile_st = os.system('g++ -std=c++17 -o {} {}'.format(bin_path, code_path))
    if compile_st > 0:
        print('compile error!')
        delete_files(bin_path)
        return [], False
    os.system('mkdir cur')
    run_st = os.system('./{} < {} > {}'.format(bin_path, data_path, output_path))

    if run_st > 0:
        print('run time error!')
        delete_files(bin_path)
        os.system('rm -rf {}'.format(output_path))
        return [], False

    ret = []
    with open(output_path, 'r') as f:
        for l in f.readlines():
            ret.append(l)

    delete_files(bin_path)
    return ret, True


def get_ans(data_path):
    ret = []
    with open(data_path, 'r') as f:
        cur = []
        for l in f.readlines():
            if l.startswith('case'):
                if len(cur) > 0:
                    ret.append(cur)
                cur = []
                continue
            cur.append(l.strip())
        cur.append(cur)
    return ret


def get_error(case, reasons):
    print('Error on case {}, msg: {}'.format(case, reasons))


def judge(results, answers):
    case_n = len(answers)
    st, tot = 0, len(results)
    for i in range(case_n):
        ans = answers[i]
        ans_n = len(ans)
        if st + ans_n >= tot:
            get_error(i+1, 'rows not match')
            return 
        for j in range(ans_n):
            if ans[j].strip() != results[st + j].strip():
                get_error(i+1, 'answer wrong, expected {}, get {}'.format(ans[j], results[st + j]))
                return 
        st += ans_n
    print('AC!')


if __name__ == '__main__':
    code_path = os.path.join(source_path, '{}.cpp'.format(args.problem_id))
    bin_path = os.path.join(source_path, 'cur')[2:]
    data_path = os.path.join(test_path, '{}.txt'.format(args.problem_id))
    output_path = os.path.join('./test/tmp', 'ret.txt')
    answer_path = os.path.join(answer_path_base, '{}.txt'.format(args.problem_id))

    results, st = get_cpp_result(code_path, bin_path, data_path, output_path)
    if not st:
        sys.exit(0)
    answers = get_ans(answer_path)
    judge(results, answers)
    