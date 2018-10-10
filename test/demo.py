a, b = 0, 1

while b < 10:
    # end可以将结果输出到同一行
    print(b,end=",")
    a, b = b, a+b