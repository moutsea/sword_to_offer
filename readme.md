## 内容

- [内容](#内容)
- [项目说明](#项目说明)
- [环境配置](#环境配置)
- [使用方法](#使用方法)
- [样例生成](#样例生成)
- [数据存储路径](#数据存储路径)

## 项目说明

创建本项目的初衷是在刷剑指 offer 等算法题时发现部分题目网上找不到对应的题目，也就没有能够测试代码准确性的地方。<br>
于是萌生了在本地搭建 judge 环境的念头。可以利用本工具在本地创建测试样例，并且进行测试。<br>
目前通过 Python 创建测试样例，C++作为算法编写语言

## 环境配置

- Python 3.6 及以上版本

## 使用方法

- 在`test_generate`下创建题目对应的生成器，如剑指 offer 第三题`3.py`
- `cd test_generate && python 3.py` 生成测试样例
- 在`./program`中创建 C++算法脚本，使用标准输入输出
- `python judge.py --problem_id 3`进行测试

## 样例生成

生成样例时只需继承`Case`类实现测试样例生成逻辑即可，其中`Case`类的定义如下：

```python
class Case:
    def output(self, path):
        raise NotImplementedError()
```

以第 3 题为例：

```python
class Case3(Case):
    def __init__(self):
        # 创建行列均有序的二维矩阵
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

    def output(self, data_path, result_path, idx):
        # 将测试数据输入data_path，答案输入result_path
        # idx为当前测试样例编号
        with open(data_path, 'a+') as f:
            f.write('{} {} {}\n'.format(self.n, self.m, self.k))
            for i in range(self.n):
                for j in range(self.m):
                    f.write('{} '.format(self.arr[i, j]))
                f.write('\n')

        with open(result_path, 'a+') as f:
            f.write('case :{}\n'.format(idx + 1))
            f.write(str(self.ans))
            f.write('\n')
```

main 函数中只需指定测试样例数量，将继承的`Case`类和题目编号传入`Generate`的构造函数即可：

```python
if __name__ == "__main__":
    generate = Generate(100, 3, Case3)
    generate.generate()
    generate.output()
```

## 数据存储路径

`./test`文件夹下有三个子文件夹，分别是`data,result,tmp`。其中`data`存储的是测试数据，`result`存储的是正确答案，`tmp`存储的是 C++代码的输出结果。
