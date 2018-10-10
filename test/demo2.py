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