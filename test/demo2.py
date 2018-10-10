def hello():
    print("你好欢迎来到python世界");


hello();


# 计算面积
def area(width,height):
    return width*height;


print(area(10,10));


def console():
    print("控制台输出。。。。")
    hello();


console();


def show(name,age):
    print("名字：",name);
    print("年龄：",age);


# 不要指定参数顺序
show(age=123, name="李四");


# 要指定参数顺序
show("刘备", 56);


# 星号表示可以传入多个参数，类型是元组,如果为空则为空元组
def one(arg1,*var):
    print(var);


one(12, 2, 3, 23);


# 以字典形式传入
def two(arg1,**var):
    print(var);


two(12,a=23,b=234,c=2345,d=23456);


# 如果参数单独出现在星号后面，param=value参数形式传入
def three(a,b,*,c):
    print(c);


three(23,23,c=10292)