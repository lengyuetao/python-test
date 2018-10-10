# 循环语句
a, b = 0, 1

while b < 10:
    # end可以将结果输出到同一行
    print(b,end=",")
    a, b = b, a+b

# 条件语句 条件如果为0则为false
number = 0;

if number:
    print("*******");
else:
    print("看看看看");


num = 1;
while num == 1:
    inNum = int(input("输入一个数字："));

    print(num)

    if inNum == 0:
        break;


