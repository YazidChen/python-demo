import random
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a = 100
b = 12.345
c = 'hello, world'
d = True

"""
使用type()检查变量的类型
"""
print('\n使用type()检查变量的类型')
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

"""
Python中的类型转换操作
"""
print('\n类型转换操作')
# 整数转成浮点数
print(float(a))  # 100.0
# 浮点型转成字符串 (输出字符串时不会看到引号哟)
print(str(b))  # 12.345
# 字符串转成布尔型 (有内容的字符串都会变成True)
print(bool(c))  # True
# 布尔型转成整数 (True会转成1，False会转成0)
print(int(d))  # 1
# 将整数变成对应的字符 (97刚好对应字符表中的字母a)
print(chr(97))  # a
# 将字符转成整数 (Python中字符和字符串表示法相同)
print(ord('a'))  # 97

"""
算数运算符
"""
print('\n算数运算符')
print(321 + 123)  # 加法运算
print(321 - 123)  # 减法运算
print(321 * 123)  # 乘法运算
print(321 / 123)  # 除法运算
print(321 % 123)  # 求模运算
print(321 // 123)  # 整除运算
print(3 ** 2)  # 求幂运算

"""
赋值运算符和复合赋值运算符
"""
print('\n赋值运算符和复合赋值运算符')
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
print(a)  # 算一下这里会输出什么

"""
比较运算符和逻辑运算符的使用
"""
print('\n比较运算符和逻辑运算符的使用')
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)  # flag0 = True
print('flag1 =', flag1)  # flag1 = True
print('flag2 =', flag2)  # flag2 = False
print('flag3 =', flag3)  # flag3 = False
print('flag4 =', flag4)  # flag4 = True
print('flag5 =', flag5)  # flag5 = False

"""
将华氏温度转换为摄氏温度
"""
print('\n将华氏温度转换为摄氏温度')
# f = float(input('请输入华氏温度: '))
f = float(100)
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

"""
输入半径计算圆的周长和面积
"""
print('\n输入半径计算圆的周长和面积')
# radius = float(input('请输入圆的半径: '))
radius = float(5)
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')

"""
输入年份 如果是闰年输出True 否则输出False
"""
print('\n输入年份 如果是闰年输出True 否则输出False')
# year = int(input('请输入年份: '))
year = 2021
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)

"""
条件语句if、elif、else
"""
print('\n条件语句if、elif、else')
x = float(0.67)
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')

"""
if嵌套结构
"""
print('\nif嵌套结构')
x = float(-1.9)
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'f({x}) = {y}')

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
print('\n判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积')
a = float(3)
b = float(4)
c = float(5)
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5  # 海伦公式
    print(f'面积: {area}')
else:
    print('不能构成三角形')

"""
用for循环实现1~100求和
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
"""
print('\n用for循环实现1~100求和')
total = 0
for x in range(1, 101):
    total += x
print(total)

"""
用for循环实现1~100之间的偶数求和
"""
print('\n用for循环实现1~100之间的偶数求和')
total = 0
for x in range(2, 101, 2):
    total += x
print(total)

"""
while循环，猜数字游戏
"""
print('\nwhile循环，猜数字游戏')

# 产生一个1-100范围的随机数
answer = random.randint(1, 100)
counter = 0
number = int(50)
while True:
    counter += 1
    if number < answer:
        number += 1
    elif number > answer:
        number -= 1
    else:
        print('恭喜你猜对了!')
        break
# 当退出while循环的时候显示用户一共猜了多少次
print(f'随机数为{answer}，你总共猜了{counter}次')

"""
嵌套循环，九九乘法表
"""
print('\n嵌套循环，九九乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()

"""
输入一个正整数判断它是不是素数
素数指的是只能被1和自身整除的大于1的整数。
"""
print('\n输入一个正整数判断它是不是素数')
num = int(7)
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

"""
两个正整数计算它们的最大公约数和最小公倍数
两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
"""
print('\n两个正整数计算它们的最大公约数和最小公倍数')
x = int(20)
y = int(25)
if x > y:
    x, y = y, x  # Python中可以用这样的方式来交换两个变量的值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break

"""
寻找水仙花数
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：13 + 53 + 33 = 153。
"""
print('\n寻找水仙花数')
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""
正整数反转，例如将12345变成54321
"""
print('\n正整数反转，例如将12345变成54321')
num = int(12345)
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

"""
百钱百鸡问题
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
print('\n百钱百鸡问题,穷举法/暴力搜索法')
# 假设公鸡的数量为x，x的取值范围是0到20
for x in range(0, 21):
    # 假设母鸡的数量为y，y的取值范围是0到33
    for y in range(0, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

"""
斐波那契数列
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，按照这个规律，斐波那契数列的前10个数是：1, 1, 2, 3, 5, 8, 13, 21, 34, 55。
"""
print('\n斐波那契数列')
# 前两个数都是1
a, b = 1, 1
print(a, b, end=' ')
# 通过递推公式算出后面的18个数
for _ in range(18):
    a, b = b, a + b
    print(b, end=' ')

"""
输入M和N计算C(M,N)
"""
print('\n输入M和N计算C(M,N)')


# 定义函数：def是定义函数的关键字、fac是函数名，numb是参数（自变量）
def fac(numb):
    """求阶乘"""
    result = 1
    for n in range(1, numb + 1):
        result *= n
    # 返回numb的阶乘（因变量）
    return result


m = int(6)
n = int(3)
# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))

"""
参数的默认值
"""
print('\n参数的默认值')


# 定义摇色子的函数，n1表示色子的个数，默认值为2
def roll_dice(n1=2):
    """摇色子返回总的点数"""
    total1 = 0
    for _ in range(n1):
        total1 += randint(1, 6)
    return total1


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))

"""
三个数相加
"""
print('\n三个数相加')


def add(a1=0, b1=0, c1=0):
    """三个数相加求和"""
    return a1 + b1 + c1


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())  # 0
# 调用add函数，传入一个参数，那么该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))  # 1
# 调用add函数，传入两个参数，1和2分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))  # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6
# 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
print(add(c1=50, a1=100, b1=200))  # 350

"""
可变参数
"""
print('\n可变参数')


# 用星号表达式来表示args可以接收0个或任意多个参数
def add(*args):
    total2 = 0
    # 可变参数可以放在for循环中取出每个参数的值
    for val in args:
        total2 += val
    return total2


# 在调用add函数时可以传入0个或任意多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
