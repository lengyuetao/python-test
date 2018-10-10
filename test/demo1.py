import sys

# 指定增量
for i in range(0, 10, 3):
    print(i);

# 遍历列表
address = ['北京', '上海', '深圳'];
for i in range(len(address)):
    print(address[i]);

# 迭代器遍历列表
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

it = iter(lists);
for i in it:
    print(i);

# next()函数迭代遍历
ss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

its = iter(ss);
while True:
    try:
        print("-----", next(its));
    except StopIteration:
        sys.exit();