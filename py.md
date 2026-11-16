# Python 学习笔记

> 适用版本：Python 3.x。内容按变量、流程控制、函数、序列和散列类型整理。

## 目录

- 一、变量与数据类型
- 二、人机交互、类型转换与运算符
- 三、流程控制（上）
- 四、流程控制（下）
- 五、函数基础（上）
- 六、函数基础（下）
- 七、函数进阶
- 八、序列类型（上）
- 九、序列类型（下）
- 十、散列类型

---

## 一、变量与数据类型

### 环境准备

#### 1. 确认 Python 已安装

在写代码之前，先确认一下自己 python 是否装好了。

打开命令行，输入 `where python`

#### 2. 创建项目（PyCharm）

![New Project 菜单](<D:/HP/Pictures/Saved Pictures/New Project 菜单.png>)

![New Project 对话框](<D:/HP/Pictures/Saved Pictures/New Project 对话框.png>)

在 New Project 对话框里需要注意：

- **Name**：项目的名字
- **Location**：项目存放的路径
- **Create a main.py file**：创建一个 main.py 文件
- **Interpreter type / Base conda**：选择自定义环境
- **Select existing**：选择已有环境
- **Python path**：绑定好你现在用解释器的位置

#### 3. print 的使用

```python
print()  # 输出/打印，将括号内的 数据 输出到命令行上
```

```python
print("hello world")
print('你好 世界')
print(33)
print(33 + 33)  # 输出66
print('33+33')  # 文本形式输出33+33
```

内容使用 ==双引号 ""==，或者 ==单引号 ''== 包围。

例如：

```python
print("Hello，world")
print('你好，我是han')
# 在python中单引号/双引号没有区别
```

**易错点：**

1. print 不需要大写 —— python 语法严格区分大小写，必须全部小写
2. Python 语法中的括号、逗号、冒号和引号必须使用英文半角符号；字符串内容仍然可以写中文。

   `。''""（）` 不要使用中文符号
   `.''""()` 使用英文符号 shift 切换

**典型错误示范：**

```python
print("Hello，world')
print('Hello，world')
print（"Hello，world"）
```

#### 4. 注释

**添加了注释的代码：**

![添加了注释的代码](<D:/HP/Pictures/Saved Pictures/添加了注释的代码.png>)

**没有注释的代码：**

![没有注释的代码](<D:/HP/Pictures/Saved Pictures/没有注释的代码.png>)

**写注释的好处：**

- 帮助调试和测试
- 提高代码的可读性

**注释的两种使用方式：**

单行注释：只能注释一行内容。若想将某一行注释，只需选中后按快捷键 `ctrl+ /`

```python
print('33+33')    #  输出'33+33'
```

Python 没有专门的多行注释语法，三引号本质上是字符串，常被临时用作多行说明。

```python
'''
注释内容
注释内容
注释内容
'''
"""
注释内容
注释内容
注释内容
"""
```

注意：解释器不执行任何的注释内容。注释可前可后。

鼓励多写注释，便于自己读代码，快速理解代码含义。

敲代码中的黄色波浪线：格式不规范，快捷键 `ctrl+alt+l`，l 是 L 的小写。

### 一、变量 ★

#### 1. 变量的概念

一句话：==存储数据的容器==

==① 变量是存储数据的容器==

==② 变量存储的数据是临时的==

==③ 变量在程序运行过程中是可以发生改变的量==

用代码的角度来看：

```python
age = 18
print(age)
print(18)
```

从右往左读：18 这个值，赋值给 age 这个变量，即把值存放到 age 这个容器里面。

#### 2. 定义变量

基本语法：

```python
变量名称 = 变量的值
```

注：Python 使用等号 `=` 作为赋值运算符。

#### 3. 命名规则

python 里面变量名字不可以乱取，需要做到==见名知意==。

```python
name = "han"
```

具体要求：

- 由数字、字母、下划线组成
- 不能数字开头
- 不能使用内置关键字，严格区分大小写

什么叫做内置关键字？就是被 python 已经定义好的单词，不能用来做你的变量名字。

可以 help 来查看 Python 的关键字（英文发明用英文写的）：

```python
help("keywords")
```

**正确命名例如：**

```python
name = "Alice"
age = 25
user_name = "bob123"

age1 = 25
user_1 = "Alice"
user_2 = "Bob"

# 区分大小写
age = 28
Age = 30  # age 和 Age 是两个不同的变量。
```

**典型错误示范：**

```python
first name = "Alice"  # 包含空格
2age = 25              # 以数字开头
if = 10  # 不能使用内置关键字if
for = "loop"  # 不能使用内置关键字for
```

注：命名尽量使用英文，不推荐使用中文，单词不会的翻译软件搜一搜，实在不行用拼音。

##### 命名法拓展（故事）

**1. 小驼峰命名法（Lower Camel Case）**

规则：第一个单词小写，后续每个单词首字母大写，其余字母小写。

适用场景：

- 变量名（`variableName`）
- 函数名（`calculateSum`）
- 对象属性（`userAge`）

例如：

```python
# 变量名
userName = "Alice"
totalScore = 100

# 函数名
calculateTotal()
getUserInfo()
```

**2. 大驼峰命名法（Upper Camel Case / PascalCase）**

规则：每个单词首字母大写，其余字母小写（包括第一个单词）。

适用场景：

- 类名（`ClassName`）

例如：

```python
# 类名
class UserProfile:
    pass
```

#### 4. 变量在内存中如何变化？

当我们执行代码：

```python
a = 10
print(a)
```

实际上在内存中：

1. 在内存中创建一个数字 10
2. 在内存中创建一个名为 a 的变量，并把它指向 10 的位置（内存地址）

![变量指向内存地址](<D:/HP/Pictures/Saved Pictures/变量指向内存地址.png>)

1 个变量只能指向 1 个内存地址。

再比如：

```python
a = 10  # a指向10
a = 20  # a重新指向20
print(a)  # 20
```

![变量重新指向新地址](<D:/HP/Pictures/Saved Pictures/变量重新指向新地址.png>)

执行上述代码，会有什么结果？

##### 举一反三

```python
a = 10
b = a
print(b)
```

![两个变量指向同一个地址](<D:/HP/Pictures/Saved Pictures/两个变量指向同一个地址.png>)

```python
a = 10
b = a
print(b)   # b打印出来就是10
```

```python
a = 10
b = 20
c = a  # c = 10
a = b  # a = 20
b = c  # b = 10
print(a)
print(b)
# a的结果是(B) b结果是(A)
# A.10  B.20  C.a  D.b  E.c
```

### 二、数据类型 ★

在 Python 里为了应对不同的业务需求，也把数据分为不同的类型。

**如何判断一个变量到底是什么类型？**

使用 `type(变量名称)` 方法，返回变量的数据类型。

print 一下出现诸如：`<class 'xxx'>`

#### 1. 整型 int

整数（int 关键字）：0-9 数字组成，比如：12, 13, 89, 100

通常可以用来记录年龄、出生年份、学生人数等整数相关动态。

举例：

```python
age = 18     # 定义一个变量age，给他一个值为18，整数int
print(type(age))  # 查看变量的类型并打印
# age = 018 是错误写法
```

注：==数字不需要加引号==。

#### 2. 浮点型 float

小数：float 类型，带小数点，比如 6.6、-6.6

举例：

```python
high = 1.8        # 定义一个人身高为1.8m
print(type(high))  # 查类型并打印  <class 'float'>
```

**补充：科学计数法**

当浮点数非常大或者非常小时，可以使用科学计数法。科学计数法使用 e 或 E 后跟指数来表示 10 的幂。

```python
# 虽然看上去是整数，但是使用科学计数法的方式，那么在程序中就是一个浮点数
print(3.14e2)   # 3.14乘以10的2次方  结果为314.0
print(3.14e-3)  # 3.14乘以10的-3次方  结果为0.00314
```

#### 3. 布尔类型 bool

布尔类型是与逻辑相关的一种数据类型，只有两个值：True 与 False（对与错，1 与 0）。

案例 1：手工定义 flag1 和 flag2 变量，其值分别为 True 和 False。

```python
flag1 = True       # 1
flag2 = False      # 0
print(flag1)       # True
print(type(flag1))  # <class 'bool'>
print(flag2)       # False
print(type(flag2))  # <class 'bool'>
```

布尔类型本质其实是数字，示例：

```python
print(1 + True)  # 2
print(1 + False)  # 1

b1 = 3 > 1  # b1 = True
print(b1)  # True
print(type(b1))  # <class 'bool'>

b2 = 3 > 4  # b2 = False
print(b2)  # False
print(type(b2))  # <class 'bool'>
```

**总结：** bool 类型就是用于代表某个事情的真（对）或假（错）。如果这个事情是正确的，用 True（或 1）代表；如果这个事情是错误的，用 False（或 0）代表。

#### 4. 字符串类型 str

字符串类型要用引号来定义，可以单引号，也可以用双引号，甚至三引号。引号引起来的值就是字符串 str。

比如：

```python
str1 = '王麻子'  # 定义一个变量str1给他一个值王麻子
print(str1)
print(type(str1))  # <class 'str'>

str2 = "王麻子"  # 双引号单引号没区别
str3 = "王 麻 子"  # 中间可以有空格
print(str2)
print(str3)
print(type(str2))  # <class 'str'>
print(type(str3))  # <class 'str'>
```

三引号定义的多行字符串，包含多行文本，非常适合存储长段落的文字。

```python
str4 = """
张三
李四
王五
赵六
"""
print(str4)  # 使用三引号定义的多行字符串，包含多行文本，非常适合存储长段落的文字。
print(type(str4))  # <class 'str'>
```

##### 字符串的运算

```python
number_01 = 66  # 定义number_01变量，给他一个值66
number_02 = '66'  # 带了引号有什么区别？

print(type(number_01))  # <class 'int'>
print(type(number_02))  # <class 'str'>

number_01 = number_01 + 1  # 右边的值给左边
print(number_01)  # number_01会等于多少？ 67

number_02 = number_02 + 1
print(number_02)  # 思考会有什么结果？如何改？  报错

number_02 = number_02 + '1' #字符串拼接
print(number_02)  # 661
print(type(number_02))  # <class 'str'>
print(number_02 * 3)  # 661661661
```

**总结：**

- 数学运算只能是数值类型，数值无法和字符串运算
- 字符串相加的实质是==串连拼接==，如果和数字相乘就转换成加法拼接
- `number_01 = number_01 + 1` 可以简写 `number_01 += 1`

---

## 二、人机交互、类型转换与运算符

### 一、input()输入方法

在python中，程序接受用户输入的数据功能即是输入。

输入是通过 `input()` 函数实现的。`input()` 函数允许用户从键盘输入内容，并将输入的值作为字符串返回。

示例：

```python
# input()引号里面的内容，就是提示要怎么去输入值或者是内容，如果你不输入的话，就会卡住，后面的代码就不会执行
name = input("请输入你的名字: ")
print(name)
print(type(name)) # input 输入的类型都是字符串
```

小测验1：请用代码模拟输入用户的年龄，并将年龄自增1,打印并输出年龄，类型

```python
age = int(input("请输入你的年龄: "))  # int()  作用就是转换数据类型成整型
age += 1  # 字符串无法和数值去做数学运算
# age = age + 1
print(age)
print(type(age)) # <class'int'>
```

小测验2：请用代码模拟输入用户的身高，并打印输出，要求结果必须是数值

```python
height = float(input("请输入你的身高: "))  # float()作用就是转换数据类型成浮点型
print(height)
print(type(height))
```

总结：

- 在python中，input()接收用户输入后,一般都会去赋值,方便后续操作，并且其==**返回值是字符串类型**==
- int()  float()  作用就是转换数据类型,int 对应整型    float 对应 浮点型
- age = age + 1  等价于 age += 1
- input本身是字符串类型，如果你要转换类型，首先要满足用户输入的值**长得像要转换的数据类型**

### 二、类型转换

数据类型转换的作用：有时候数据需要转换为另一种类型去做逻辑处理，可以类型转换

4个类型：int float bool  str 可以互相转换

#### 1.基本方法：

```python
"""
int(变量):把变量转换成一个整数
float(变量):把变量换成一个浮点类型数据
str(变量):把变量换成字符串类型
bool(变量):把变量换成布尔类型
"""
```

#### 2.示例：

- 超市找零系统

```python
"""
 程序输入  商品单价price 商品数量count 支付金额money
 程序输出  找零result
"""
# 超市找零系统
# result = money - price * count
price = float(input("请输入商品价格："))
count = int(input('请输入商品数量：'))
money = float(input('请输入所支付的金额：'))
result = money - price * count
print(result)
```

- 布尔类型转数字

```python
# True 就是1  False 就是0
print(True + 1)  # 2
print(False + 1)  # 1
# 转型用int()与float()
print(int(True))  # 1
print(int(False))  # 0
print(float(True))  # 1.0
print(float(False))  # 0.0
```

- 其他类型转布尔

```python
print(bool(1))  # True
print(bool(10086))  # True
print(bool("原神启动"))  # True
# 常见 False 值包括 0、0.0、空字符串、空容器和 None
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(""))  # False
print(bool(" "))  # True " "不是空字符串,空字符串指字符串内无一切内容
```

- 小数与 整数互转

```python
a = 1.999999
print(int(a))  # 小数转整数不是四舍五入而是保留整数部分
a = 23
print(float(a))  # 23 → 23.0
print(f"{a:.2f}")  # 保留2个小数点
```

一些例题：

```python
print(int('10') * 3) # 30
print(int('25') + int('25')) # 50
print(str(111) + str(99)) # 11199
print(str(55) * 3) # 555555
print(int('8') > 10) # False
print(str(10) == 10) # False
print(bool("") == bool(0)) # True
```

### 三、print()输出拓展

print()   打印输出    了解拓展用法

```python
# 1.print 可以同时输出多个值
name = "张三"
age = "18"
sex = "男"
print(name, age, sex)  # 输出多个值

# 2.上述例子中不想用空格隔开怎么办？
print(name, age, sex, sep="@")  # 一次性输出多个值，值用@隔开
print(name, age, sex, sep="~")  # 一次性输出多个值，值用~隔开
print(name, age, sex, sep="\n")  # 一次性输出多个值，值用换行隔开

# 3.如何将下面两行代码合并为一行？
print("Hello")
print("World")
# 传递参数 end="" 效果是以空字符串连接两个print()的内容
print("Hello", end="")
print("World")
# end="," 效果是以逗号连接两个print()的内容
print('hello', end=',')
print('world')
```

拓展：

#### 1.格式化输出

```python
# 第一种方式:print(变量名)    (了解)
# 第二种方式:%()             (了解)
# 三:(f"{}")方式输出         (掌握)
# 四:format()               (了解)
#     了解是能看懂就行，掌握必须要会用
# 定义三个变量
name = "小美"
age = 18
price = 1.2
# 我叫小美,今年18,我去超市买了单价1.2元/斤的白菜# 第一种方式
print('我叫', name, ',今年', age, ',我去超市买了单价', price, '元/斤的白菜', sep='')
# 第二种方式:%()             (了解)
'''
%s 字符串类型的数据
%d  整数
%f  float类型
%.xf x表示整数，表示要保留几位小数点
'''
print("我叫%s,今年%d,我去超市买了单价%.1f元/斤的白菜" %(name, age, price))
# (f"{}")方式输出            (掌握)
print(f"我叫{name},今年{age},我去超市买了单价{price}元/斤的白菜")  # 一一对应
# format()                  (了解)
print("我叫{},今年{},我去超市买了单价{}元/斤的白菜".format(name, age, price))  # 一一对应
```

#### 2.转义字符 \

由反斜杠加上一个字符或数字组成，它把反斜杠后面的字符或数字转换成特定的意义。常用的有：

- \n：换行。
- `\t`：制表符，一个tab键（4个空格）的距离。
- \'  :  字符串单引号
- \" :  字符串双引号
- \\ :   字符串\

```python
print('张三\n李四\n王五\n赵六')
s0 = '\t'
print(s0)
s1 = '\"'  #也可以直接 s1 = '"'
print(s1)
s2 = '\\'  #不能直接 '\'
print(s2)
s3 = '\''  #也可以直接 s2 = "'"
print(s3)

```

### 四、运算符★

#### 4.1算术运算符

用来完成基本的算术运算的符号，简单来说就是四则运算的符号，在Python中的算术运算符有如下几种：

| 运算符 | 说明                                | 实例        | 结果  |
| ------ | ----------------------------------- | ----------- | ----- |
| +      | 加                                  | 12.45 + 15  | 27.45 |
| -      | 减                                  | 4.56 - 0.26 | 4.3   |
| *      | 乘                                  | 5 * 3.6     | 18.0  |
| /      | 除法（和数学中的规则一样）÷         | 7 / 2       | 3.5   |
| //     | 整除（只保留商的整数部分）          | 7 // 2      | 3     |
| %      | 取余，即返回除法的余数              | 7 % 2       | 1     |
| **     | 幂运算/次方运算，即返回 x 的 y 次方 | 2 ** 2      | 4     |

```python
# 1.算数运算符
print(10 + 3.1)
print(10 + 3)
print(10 / 3)  # 除 结果带小数
print(10 // 3)  # 只保留整数部分 商  3
print(10 % 3)  # 取模、取余数   1
print(10 ** 3)  # 10的三次方 10 * 10 * 10  ^
```

注：混合运算优先级顺序： () 高于 ** 高于 * / // % 高于 + -

#### 4.2赋值运算符

| 运算符 | 说 明      | 用法举例 | 等价形式   |
| ------ | ---------- | -------- | ---------- |
| =      | 赋值运算   | x = y    | x = y      |
| +=     | 加赋值     | x += y   | x = x + y  |
| -=     | 减赋值     | x -= y   | x = x - y  |
| *=     | 乘赋值     | x *= y   | x = x * y  |
| /=     | 除赋值     | x /= y   | x = x / y  |
| %=     | 取余数赋值 | x %= y   | x = x % y  |
| **=    | 幂赋值     | x **= y  | x = x ** y |
| //=    | 取整数赋值 | x //= y  | x = x // y |

增量赋值

```python
# 增量赋值 , 基于自己修改
level = 1
print(level)
level += 1  # level = level + 1
print(level)
level += 3  # level = level + 3
print(level)
# 类似的
a = 1
a += 1  # 等价 a = a + 1
a *= 3  # 等价 a = a*3
a /= 3  # 等价 a = a/3
```

单个变量赋值

```python
num = 1
print(num)
```

多个变量赋值

```python
num1, float1, str1 = 10, 0.8, 'man tian'
print(num1, float1, str1)
```

链式赋值--定义多个相同的变量

```python
x = y = z = 10  # 同时定义了3个变量，都是10
print(x, y, z)
```

交叉赋值--实现值的互换

```python
# 方法一
a = 1
b = 2
c = a
a = b
b = c
# 方法二
a, b = b, a
print(a)
print(b)
```

#### 4.3 比较运算符

比较运算符， 就是用来比较的，有比较就有结果。所以比较运算符结果一定是布尔值

| 比较运算符 | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| >          | 大于，如果>前面的值大于后面的值，则返回 True，否则返回 False。 |
| <          | 小于，如果<前面的值小于后面的值，则返回 True，否则返回 False。 |
| ==         | 等于，如果==两边的值相等，则返回 True，否则返回 False。      |
| >=         | 大于等于（等价于数学中的 ≥），如果>=前面的值大于或者等于后面的值，则返回 True，否则返回 False。 |
| <=         | 小于等于（等价于数学中的 ≤），如果<=前面的值小于或者等于后面的值，则返回 True，否则返回 False。 |
| !=         | 不等于（等价于数学中的 ≠），如果!=两边的值不相等，则返回 True，否则返回 False。 |

```python
age = 18
print(age > 18)  # False
print(age < 18)  # False
print(age == 18)  # True
print(0 <= age <= 100)  # True
"""
判断一个数是不是偶数
8 % 2 == 0  T
9 % 2 == 0  F
中文：如果一个整数 跟2 求余数 结果为0，那么这个数一定是偶数
中文：如果一个整数 跟2 求余数 结果为1，那么这个数一定是奇数
"""
number = int(input('请输入一个数，我可以判断他是不是偶数：'))
print(number % 2 == 0)  # 偶数输出True 奇数输出Fasle
```

#### 4.4 逻辑运算符

布尔类型的运算，结果一定也是 布尔值

| 逻辑运算符 | 含义                           | 基本格式 | 说明                                                         |
| ---------- | ------------------------------ | -------- | ------------------------------------------------------------ |
| and        | 逻辑与运算，等价于数学中的“且” | a and b  | 当 a 和 b 两个表达式都为真时，a and b 的结果才为真，否则为假。 |
| or         | 逻辑或运算，等价于数学中的“或” | a or b   | 当 a 和 b 两个表达式有1个为真，a or b 的结果就是真，否则为假。 |
| not        | 逻辑非运算，等价于数学中的“非” | not a    | 如果 a 为真，那么 not a 的结果为假；如果 a 为假，那么 not a 的结果为真。相当于对 a 取反。 |

```python
a = 0
b = 1
c = 2
# 1.and: 与 ：都真才真
print(a < b and c > b)  # True
print(a > b and c > b)  # False
# 2.or 或 一真都真，都假才假
print(a < b or c > b)  # True
print(a > b or c < b)  # False
# 3.not ：非 /取反
print(not False)  # True
print(not c > b)  # False
```

#### 4.5 身份运算符

身份运算符在编程语言中用于比较两个对象是否引用同一个内存地址，而不是它们的值是否相等。

is 运算符

- 用于判断两个变量是否指向同一个内存地址。
- 如果是同一个对象，返回 `True`；否则返回 `False`。

```python
# 身份运算符
a = 10086
b = a
print(a is b)  # True,因为b和a指向同一个内存地址
print(a == b)  # True,因为 == 比较的是值
```

| 运算符 | 描述                                        | 实例                                                         |
| ------ | ------------------------------------------- | ------------------------------------------------------------ |
| is     | is 是判断两个标识符是不是引用自一个对象     | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

我们可以用 id() 来判断两个变量是否指向同一个内存地址。 我们可以将id值理解

为那块内存的地址标识。

```python
x = "张三"
y = '李四'
print(id(x))  # x的内存地址标识
print(id(y))  # y的内存地址标识
print(x is y)  # 效果等价于id(x) == id(y)
```

#### 4.6 优先级

从最高到最低优先级的所有运算符

| 运算符说明 | Python运算符         | 优先级 | 结合性 |
| ---------- | -------------------- | ------ | ------ |
| 小括号     | ( )                  | 19     | 无     |
| 乘方       | **                   | 16     | 右     |
| 符号运算符 | +（正号）、-（负号） | 14     | 右     |
| 乘除       | *、/、//、%          | 13     | 左     |
| 加减       | +、-                 | 12     | 左     |
| 比较运算符 | ==、!=、>、>=、<、<= | 7      | 左     |
| is 运算符  | is、is not           | 6      | 左     |
| 逻辑非     | not                  | 4      | 右     |
| 逻辑与     | and                  | 3      | 左     |
| 逻辑或     | or                   | 2      | 左     |

优先级顺序：

- 算数优先级大于比较运算符

```python
b = 2 + 10 > 11
print(b)
#True
```

- 比较运算符优先级大于逻辑运算符

```python
b = 1 > 2 and 2 < 10
print(b)
#False
```

- 逻辑运算符内部三个优先级 not > and > or

```python
b = not True and 1 > 2 or 3 == 8
print(b)
#False
```

总结:

1. 先乘除后加减，括号优先2. 算数优先级 > 比较运算符 > not > and > or

```python
# 在 Python 中，input() 函数的返回值是什么数据类型？(C)
- A. int
- B. float
- C. str
- D. bool

# 以下代码输出什么? ()
a = 10
b = 20
print(a, b, sep='-', end='*')
print(a + b)
#输出：
10-20*30

-
# 以下代码输出什么？(A)
print(
    (3 + 5 > 7 and 2 * 3 < 5) or
    (not 4 == 4 and 6 / 2 > 2) or
    (8 - 3 == 5 and not 0 > 3)
)
# not 0 > 3 是not（0 > 3）
- A. True
- B. False

# 以下类型转换表示正确的是？  ()
- A.  int(6.9)  结果为 7 # 直接砍掉小数部分
- B.  bool("False") 结果为 False # 错误：非空字符串为 True；空容器和 None 也是 False
- C.  bool(0) 结果为 True #结果为False
- D.  bool(1) 结果为 True
```

---

## 三、流程控制（上）

在程序中流程就是代码执行的过程

在Python当中主要的流程分3大结构：顺序结构(目前)、分支结构、循环结构

- 顺序结构：程序从头到尾的顺序依次执行每一条 Python 代码。
- 分支结构（选择结构）：程序有选择性的往下执行，相当于有了路A和路B，可以依靠判断条件布尔值来选择执行2条或者以上的路径
- 循环结构：程序可以选择回头，不断地重复执行同一段代码。

### 3.1分支结构

概念解释与基础

`if` 是一个用于控制程序流程的 条件语句，用于根据条件的真或假来决定是否执行某段代码。

如果条件满足，就执行相应的代码块；如果不满足，就跳过这段代码。

假设一个场景：

- 你去网吧上网，成年了吗？
- 成年了，可以上网
- 未成年，好好学习其实这里所谓的判断就是条件语句，即条件成立执行某些代码，条件不成立则不执行这些代码。

在Python中，if语句的基本语法是这样的

语法结构

```python
if 条件判断:
    条件为True执行的代码区域
    条件为True执行的代码区域
    条件为True执行的代码区域
    ....
```

==缩进结构==

Python 的代码结构确实非常独特，其创始人 龟叔 (确实是个人物) 设计了通过缩进来组织代码块的规则，这不仅提升了代码的可读性，也帮助程序员养成良好的编程习惯。

所以python中的缩进是有特殊含义的，表示语句块的进入和退出，不可以随便使用空格和缩进。

```python
print("hello,world")  # 这行代码可以输出 hello，world
    print("hello,world")  # 但是这行会报错！  不可以随便在前面空出格子
```

python通过 缩进(tab键) 来表示里外结构

```python
# 缩进配合if来表示语句块的进入
if 条件判断（bool）:
    表示if内部，条件判断成立进入的代码  # 增加缩进，进入
if
表示if外部，与if无关的代码  # 取消缩进，结束if
```

在清楚了缩进后，python分支结构 之 单向分支

#### 3.1.1 if单分支★

在现实生活非常常见，比如 我们的年龄，如果年龄≥18岁了 (未成年人喊个成年人也可以去) ，是不是就可以上网吧，和防沉迷了。这就是一个典型的分支。把年龄分为  成年和未成年

```python
age = int(input('enter your age: '))
if age >= 18:
    print("恭喜你，成年了")
print('恭喜你，可以上网了')
print('这是if外部的代码')
"""
代码细节：
    1. if 即为分支的语法， 可以理解为如果
    2. age >= 18 为判断条件，if的后面必须为布尔类型
    3. 注意if age >= 18 后面要加上冒号 :    表示要进入缩进代码块了
    4. print("恭喜你，成年了")  # 一定要加上缩进，当条件判断为True时执行，False则不执行
"""

# 经典错误:
age = int(input('enter your age: '))
if age >= 18:
print("恭喜你，成年了")
"""
程序会报错，为什么？
上述print语句并没有进行一个缩进,也就是说它和if是同级别关系,并不是内外关系.
所以if并没有语句块,在python中,必须要写缩进的地方,如果不写代码,会报错.
"""
```

if总结:

- 代码块由相同缩进量的若干条语句组成。
- 缩进通常用一个tab键
- 没有缩进的代码块跟if条件判断无关
- ==if语句的最后要有有冒号== :       不要忘记！！！

#### 3.1.2 if..else 双分支

作用：条件成立执行if下方的代码，条件不成立执行else下方的代码

- if-else语句的语法结构

```python
if 条件布尔值:
    条件成立中执行的代码1
    条件成立执行的代码2
    ......
else：
    条件不成立中执行的代码1
    条件不成立执行的代码2
    .....
中文理解： if(如果)  else(否则)
# 成绩 >=60  及格 否则就 不及格
score = float(input('请输入你的成绩: '))
if score >= 60:
    print('及格')
else:
    print('不及格')
注意：双向分支只会执行其中1个分支，不可能同时输出  及格和不及格
```

网吧上网的实例，如果成年，允许上网，如果不成年呢？是不是应该回复用户不能上网？

```python
age = int(input('Enter your age: '))
if age >= 18:
    print('可以上网')
else:
    print('好好学习')
```

注意：如果条件成立执行了某些代码，那么其他情况的代码将不会被执行

#### 3.1.3 多分支

生活中有时候有多种可能，不一定是双向，比如某次期末成绩分数可以这样分层：

80-100：优秀

60-80：及格

60分以下：不及格

- 基本语法：

```python
# 从上往下判断，如果为true了就不会再往下执行了
if 布尔值1:
    执行语句1
elif 布尔值2:  # elif 是 else if 的缩写   意思为 否则如果
    执行语句2
else:
    执行语句3

# 示例演示：
score = float(input('请输入你的成绩：'))
if 80 <= score <= 100:
    print("优秀")
elif 60 <= score:
    print('及格')
else:
    print('不及格')

```

- elif可以有0个或多个。
- else可以有0个或1个，且只能放在if语句的最后。

举一反三：生活费

```python
money = float(input("请输入你的生活费："))
if money >= 2000:
    print('有点多')
elif money >= 1200:
    print('合适')
else:
    print('有点少')
```

#### 3.1.4 嵌套分支

嵌套就是套娃

这里面的每个娃娃就像if语句结构

if语句成立和不成立所执行的代码块，依旧是写我们正常的代码，也就是说支持再写if

- 示例:

```python
if 表达式1:
    if 表达式2:
        if表达3
    else:
        语句块3
else:
    语句块1
```

![流程控制示意图](<assets/day03_img/day 3_p07-flowchart.png>)

对于if语句可以有多种嵌套方式，在开发程序时可以根据自己的需要来选择合适的嵌套方式，但一定要严格控制好缩进

比如，在输入成绩之前，要求成绩必须要为正数

```python
score = float(input('请输入你的成绩：'))
if score >= 0:  # 如果不是正数，没有必要去判断阶段了，因为这种输入是错误的，跳到最下面的else
    if 80 <= score <= 100:
        print("优秀")
    elif 60 <= score:
        print('及格')
    else:
        print('不及格')
else:
    print("请输入正确成绩")
```

- 注意：嵌套分支了一定要注意缩进结构!!!
- 案例：  购物打折计算

```python
"""
    编写一个程序
        用户输入 商品单价，购买数量，付款金额
        程序输出 打折后找零多少钱
    打折制度
    如果购物金额超过100元但不超过200元，享受9折优惠
    如果购物金额超过200元但不超过500元，享受8折优惠
    如果购物金额超过500元，享受7折优惠
    100元及以下不打折

"""
price = float(input('请输入价格：'))
count = int(input('请输入数量：'))
money = float(input('请输入付款金额：'))
# 购物总金额
total = price * count
if total >= 0:
    if total <= 100:
        total = total * 1
    elif total <= 200:
        total = total * 0.9
    elif total <= 500:
        total = total * 0.8
    else:
        total = total * 0.7
    result = money - total
    print(result)
else:
    print('请输入正确的商品信息')
```

#### 3.1.5 三目运算符

也叫三元运算符  ，可以简洁 if语句写法，一行实现分支结构

语法如下：

```python
# 标准版
if 条件表达式:
    成立的时候执行的代码
    ...
else:
    不成立的时候执行的代码
    ....

# 三目版
成立的时候执行的代码 if 条件表达式 else 不成立的时候执行的代码
```

快速体验 （坐飞机）：

```python
"""
语法
   条件成立执行的代码 if 条件 else 条件不成立执行的代码"""
# 标准版
age = 19
if age >= 18:
    print("成年")
else:
    print("未成年")

# 三目运算符版
age = 19
print("成年") if age >= 18 else print("未成年")# 也可以在赋值的时候运用
age = 19
str1 = "成年" if age >= 18 else "未成年"
print(str1)  # 成年 or 未成年
```

#### 3.1.6 pass关键字

在 Python 中，`pass` 是一个用于表示“什么都不做”的**占位符**关键字。

它的主要作用是**占位**，以便代码的结构能够正确运行，即便某些地方暂时没有任何具体实现。

- 登录案例

```python
"""
    假如账号是 'root'
    密码是 '123456'

    用户输入账号和密码，程序输出 登录成功
"""
# 方法一
username = input('请输入账号：')
password = input('请输入密码：')
if username == 'root' and password == '123456':
    pass  # 什么都不做，占个坑，保持程序结构性
else:
    print('账号或者密码错误')

```

实际开发中，有时候我们会先搭建起程序的整体逻辑结构，但是暂时不去实现某些细节，而是在这些地方加上一些

注释，方便以后再填写代码，比如：

```python
age = int(input('你的年龄:'))
if age >= 18:
    print("可以去网吧打游戏了！")
else:
    pass  # 暂时还没想到要写什么,填个pass吧,因为不填会报错.
```

注:必须要写缩进的地方，如果不写代码,可以用pass占个位,这样就不会报错!!

### 3.2 循环结构★

如果希望把hello world 输出2遍

```python
print("hello wolrd")
print("hello world")
```

很简单只需要2行代码，那如果输出100遍呢？似乎变得麻烦了。

循环可以让这个麻烦的事情变得简单，让一段代码反复执行。

在python编程语言中循环有2种，一种是while循环，一种是for循环。

#### 3.2.1 while循环（条件循环）

while循环是通过 条件判断 来控制循环次数的，和if有点类似

```python
if 条件表达式:
    代码块

while 条件表达式:
    代码块(循环体)
```

现在来执行一段代码

```python
if 0<3:
    print("hello world") # 只会执行一次

while 0<3:
    print("hello world") # 会一直执行！

if 在条件成立的时候 会进入if的代码区域

while 在条件成立时 也会进入while的代码区域，但while与if不同，会反复输出里面的代码

什么时候结束呢？当条件表达式为False的时候结束

观察这个式子发现True是绝对的不会改变，那就会永远执行下去，我们称这种循环为 死循环。
希望循环可以可控的，可以将 条件表达式 化为变量
a = 0
while a < 3:
    print('hello world')
# 依旧为死循环，因为条件不变，改为变量的目的就是让True一步一步靠近False
a = 0
while a < 3:
    print('hello world')
    a = a + 1
    print(f'a={a}')

"""
输出效果如下:
hello world
a=1
hello world
a=2
hello world
a=3
"""
解释：上述代码会打印3次消息，每次循环a值增加1，直到a不再小于3时循环停止。

使用while循环想要达到可控的目的需注意:
"""
    1.定义循环外的变量
    2.用变量去写判断条件
    3.循环过程中通过修改变量，靠近出口,走出循环体"""
```

#### 3.2.2 debug运行模式

所谓bug，就是程序中的错误。如果程序有错误，需要程序员排查问题，纠正错误。

所谓debug，就是调试模式运行，程序会在 断点 处停留，方便测试和分析

打断点：觉得哪里不清晰，可能出问题，打个断点停留分析

Debug 过程中能够深入理解程序的运行机制和潜在问题

- 应用一： 输出 1~100

```python
print(1)
print(2)
....
print(100)
# 上述代码非常麻烦，那就用循环来做
a = 1
while a < 101:
    print(a)
    a += 1
```

- 应用二：计算1+2+3+4+....100

```python
# 需求：1-100数字累加和---1+2+3+4+5+....100 =结果，打印结果
"""
1.准备做加法运算的数据 1~100增量为1的数字
2.准备一个变量来保存将来运算的结果
3.循环来做加法运算
4.打印结果
5.验证结果
"""
# 在循环之上，定义一个初始累计变量
c = 0  # 初始为0
a = 1
while a < 101:
    c = c + a
    a = a + 1
    print(f'a={a},c={c}')
print(c)
# c = 0 + 1
# c = 0 + 1 + 2
# c = 0 + 1 + 2 + 3
# c = 0 + 1 + 2 + 3 + 4
# c = 0+1+2+3+...99 + 100
```

- 应用三：输出1~100中的偶数
- 应用四：输出1~100中偶数的和 （学会累乘）
- 应用五：统计1~100中的偶数的数量 （学会计数）

```python
1. 输入一个整数，如果这个是正数则输出正数，如果是负数输出负数，如果是0输出0
2. BMI是世界公认的一种评定肥胖程度的分级方法，世界卫生组织(WHO)也以BMI来对肥胖或超重进行定义。
  BMI是以你的身高体重计算出来的,它的定义如下：
   体重指数(BMI)=体重(kg)÷身高**2(m)
  成人的BMI数值：
  过轻：低于18.5
  适中：18.5-25
  过重：25-30
  肥胖：30-35
  非常肥胖,高于35

   请你设计一款程序,用户输入体重(kg单位),输入身高(m单位),就可以计算出BMI然后根据BMI再输出 过轻 适中 过重 肥胖 非常肥胖

3. 输入一个数，如果这个数是偶数 输出 偶数 否则输出奇数
4. 使用while循环 输出 1 到 100
```

---

## 四、流程控制（下）

### 4.1 循环结构

- 应用三：输出1~100中的偶数

```python
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i +=1
```

- 应用四：输出1~100中偶数的和

```python
res = 0  # 初始为0
count = 1
while count < 101:
    if count % 2 == 0:
        res = res + count
        print("过程中的：", res)
    count += 1
# 以下的代码，都是在100次循环之后执行
print(count)
print('循环结束后的:', res)
```

应用五：学会在循环中计数（计数器）

```python
# 统计1~100中，3的倍数有多少个？
count = 0  # 该变量用于计数,表示3的倍数的个数
i = 1
while i < 101:
    if i % 3 == 0:
        count += 1
    i += 1
print(count)
```

#### 4.1.3 for循环(迭代)

for循环和while循环本质没有什么区别。

语法

```python
for 变量名 in range(start,end):
    循环体

range(start,end) （包头不包尾）前闭后开     [1,100)
```

- 输出1~100

```python
# 输出 1~100
for i in range(1, 101):  # 包头不报尾  [1，101)
    print(i)
```

- 计算1+2+3+。。。。100

```python
res = 0  # 初始累计变量
# 输出 1~100
for i in range(1, 101):
    res += i
print(res)
```

for循环拓展

```python
"""
range的第三个参数，是步长，可以控制 start ~ end-1 的间隔
for 变量名 in range(start,end,step=1):
    循环体
"""

range(1, 101, 1)  # 1 2 3 4 ...     100
range(1, 101, 2)  # 1 3 5 7 9    ... 99
# range的起点也可以默认
# 如果range只填了1个值，那么这个值就表示结束值，起点默认是0，步长默认是1
for i in range(10):  # range(0,10)
    print(i)  # 0~9

# 思考:可不可行?
# 输出0-10内的偶数
for i in range(11, 2):
    print(i)  # 不行
```

举一反三:

- 用for循环输出1~100中的偶数

```python
for i in range(2, 101, 2):
    print(i)

```

- 用for循环输出1~100中偶数的和

```python
# 输出1~100
res = 0
for i in range(2, 101, 2):
    res += i
print(res)
```

- for循环中的计数（计数器）

```python
count = 0
# 统计下列循环会循环多少次？
for i in range(2, 11, 2):
    count += 1  # 每循环一次加个1
print("结束后count的值为：", count)  # 5
```

#### 4.1.4 break和continue

主动控制循环退出的两种方式

break: 退出整个循环

continue: 退出本次循环，继续执行下一次循环猴子 吃 10 个苹果

1. 猴子吃的过程中，吃到第3个苹果，吃饱了。 吃苹果的循环就可以结束了，这就类似于  break，结束整个循环2. 猴子吃的过程中，吃到第3个苹果，吃到了一只毛毛虫，扔掉，继续吃第4，5，6，7，8，9，10 结束， 类似程序中的continue

```python
for i in range(1, 11):
    if i == 3:
        break
    print(i)
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

```

- 登录功能的改进

```python
# 账号：root   密码：123456
"""
    程序运行的时候提示登录，输入账号和密码
        如果正确，则提示登录成功
        如果错误，则提示重新输入账号密码
"""
# 请对一下代码做出更改,要求更改后的代码可以反复登录,直到登录成功为止
username = input('请输入账号：')
password = input('请输入密码：')
if username == 'root' and password == '123456':
    print('登录成功！')
else:
    print('账号或者密码错误')

# 法一
while True:
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'root' and password =='123456':
        print('登录成功！')
        break  # 直接结束当前循环
    else:
        print('账号或者密码错误')

# 法二
flag = False  # 利用变量来标识 登录状态 True标识登录，False标识未登录
while not flag:
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'root' and password =='123456':
        print('登录成功')
        flag = True
    else:
        print('登录失败,请重新输入')

# 修改之后的代码还存在安全隐患,如果限制用户只有三次登录机会,该怎么修改代码?
count = 0
for i in range(3):
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'root' and password =='123456':
        print('登录成功！')
        break
    else:
        print('账号或者密码错误')
        count = count + 1
        if count == 3:
            print('三次机会已用完，请24小时后再尝试')

count = 0
while count < 3:
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'root' and password =='123456':
        print('登录成功！')
        break
    else:
        print('登录失败')
        count += 1
        if count == 3:
            print('三次机会已用完，请24小时后再尝试')
```

#### 4.1.5 循环else(用得少)

```python
if 条件布尔值:
    True执行的代码
else:
    False执行的代码

# 举例：
for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:  # 循环正常结束，没被break强制退出，则执行后续代码
    print("循环执行完毕执行的代码")

# 登录案例：
for i in range(3):
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'root' and password =='123456':
        print('登录成功！')
        break
    else:
        print('登录失败')
else:
    print('三次机会已用完，请24小时后再尝试')

```

#### 4.1.6 循环嵌套

```python
for i in range(2):
    for j in range(5):
        print("hello,world")

a = 0
for i in range(2):
    for j in range(5):
        print(f"i={i},j={j}")
        a += 1
print(a)

```

- 求3位数的所有可能性，并逐个打印输出100-999
- x 表示 百位
- y 表示 十位
- z 表示 个位

```python
for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            print(x, y, z)
```

```python
'''
1.
说到回文数，可能会比较的陌生，但是在我们的日常生活中常会遇到这样的数字，只是你不知道它是回文数罢了。
例如：121、212、101，这组数字就是回文数。指正向和逆向相等的数字。
请输出100~999之间的回文数

2.假设一张足够大的纸，纸张的厚度为0.5毫米。请问对折多少次以后，可以达到珠穆朗玛峰的高度(最新数据：8844.43米)。请编写程序输出对折次数。
ps:1mm = 0.001m
   0.5mm = 0.0005m
    while
    计数
'''
3.九九乘法表
```

![九九乘法表](<D:/HP/Pictures/Saved Pictures/day 04_p10-diagram.png>)

---

## 五、函数基础（上）

### 5.1 函数介绍

函数：组织代码、执行特定任务的工具

作用：将可重复执行的代码块封装起来，通过函数调用来使用这些代码。

像print(),input(),len(),max(),min(),sum() 这些都是Python内置函数

#### 5.1.1 函数组成

一个函数通常由以下几个部分组成：

1. 函数名：标识函数的名称，用于在调用时引用该函数。

2. 参数：函数可以接受参数，参数是传递给函数的信息。参数在函数定义时指定，函

- 数调用时传入。

3. 函数体：包含执行的代码块，是函数的主要部分，定义了函数执行的任务。

4. 返回值★：函数可以返回一个值，通过 `return` 语句实现。返回值可以是函数计算

- 的结果，也可以是操作状态的指示。
- 函数定义的基本语法：

```python
def 函数名(参数):
    代码块
    代码块
    代码块
    return result  # 可选，返回一个值，如果不加return，则默认返回None
感受封装的好处：
# 每把农药的游戏是不是有这样的开场提示？
def func():
    print("敌军还有三十秒到达战场")
    print("全军出击")
不可能每一场对局都重新去写一遍代码，而是想用的时候直接去调用。
```

- 总结优点
- 重复的功能，可以直接调用，减少代码量提升代码的结构性，分工明确，提高可读性拓展和维护的时候非常方便

### 5.2 命名规则

在 Python 中，函数命名需要遵循一定的命名规则和最佳实践。以下是一些常见的命名规范：

1. 蛇形命名法（snake_case）： 采用小写字母和下划线的命名方式。例如：

```python
def calculate_area():
    pass
```

2. 避免使用 Python 关键字： 函数名不能与 Python 的保留字或关键字冲突，如 `def`、`class`、`if` 等。

3. 见名知意： 函数名应当能够清晰表达其功能，避免使用无意义或过于简短的名称。例如：

```python
def get_user_name():
    pass
```

- 而不是：

```python
def foo():
    pass
```

4. 避免使用大写字母： 通常函数名应避免使用大写字母。大写字母通常用于类的命名（驼峰命名法）。例如：

```python
def process_data():  # 正确
def ProcessData():  # 不建议,通常类名使用驼峰命名法
```

5. 长度适中： 函数名应适当简洁，但也要避免过于简短或冗长。它应该清晰地表明函数的作用。

命名的简单总结：

```python
- 由数字、字母、下划线组成
- 不能由数字开头
- 不能是关键字  if  print while for
- 见名知意
- 蛇形命名法

经典错误：
def 123func():
def if():
def func go():
def Func():
```

### 5.3 调用函数★

```python
def func():
    print("敌军还有三十秒到达战场")
    print("全军出击")
print(func) #  内存地址
print(type(func))# <class function>  是一个函数# 回忆一下，之前是怎么调用函数的？
print()
input()
len()
sum()
type()
....
其实这些内置函数   print、input、len、sum、type就是函数名
如果你只输入函数名，是无法执行函数的。
调用语法：
    函数名()

fn() # 带了()才会执行函数封装好的代码
演示：
def func():
    print("敌军还有三十秒到达战场")
    print("全军出击")
func()
func()
```

- 区分一个东西 ★

```python
func    是什么     函数对象  表示地址位置，地址可以传递
func()  是什么     调用函数
print   是什么     函数对象 表示地址位置，地址可以传递
print() 是什么     调用函数
# 函数的地址可以传递举例：
x = print  # 将x变为print函数
x("hello,world")  # 等价于 print("hello,world")
```

- 练习：定义一个login函数，功能是 输入用户名和密码，验证是否正确

```python
def login():
    username = input('输入用户名:')
    password = input('输入密码:')
    return username == 'root' and password =='123456'
print(login())
```

### 5.4 函数参数★

#### 5.4.1 形参和实参

- 无参函数：括号什么都不写

```python
def 函数名():
    代码块

函数名()  # 调用函数执行代码块
```

- 有参函数：括号里面可以填写参数(形参)

```python
def 函数名(形参1,形参2,形参3…):
    代码块

函数名(实参1，实参2，实参3…)  # 调用函数，把实参传给形参，执行代码块
```

- 形参：全名形式参数，没有值。
- 实参：实际参数， 实参是在调用函数时传递给函数的具体值。举例

```python
# 创建一个函数，实现2个参数的和
def jia(a, b):  # 形参a,b
    print(a + b)
jia(10, 20)  # 这里的10和20就是实参,调用函数sum的同时,实参传递给形参a,b最终输出30
jia("hello", "world")  # 调用函数sum并传递实参'hello' 'world' 输出 'helloworld'
```

总结： 形参本身没有值，函数调用的时候，实参把值传递给形参.

#### 5.4.2 位置参数与关键字参数

在传递实参时，有两种常见的方式：位置参数和关键字参数。

- 位置参数：实参的值根据位置对应传递给形参。
- 关键字参数：通过形参的名称来明确传递实参值。

位置参数示例:

```python
def greet(name, age):
    print(f"Hello, 我是{name}! 今年{age}岁.")

greet("Alice", 30)  # "Alice" 和 30 是位置参数
```

关键字参数示例:

```python
def greet(name, age):
    print(f"Hello, 我是{name}! 今年{age}岁.")

greet(age=30, name="Alice")  # 通过关键字传递实参
```

混合使用示例:

```python
def greet(name, age):
    print(f"Hello, 我是{name}! 今年{age}岁.")
greet('man tian', age=18)  # 注意位置传参和关键字传参可以混合使用
# 混合使用需要注意顺序
def fn(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)
fn(1, c=3, b=2)  # 混合使用,先位置参数,后关键字参数
fn(a=1, 2, 3)  # 报错不可以先用关键字参数，注意顺序
```

#### 5.4.3 默认值参数

函数形参可以有默认值，如果调用时没有传入该参数，函数会使用默认值。

示例:

```python
def greet(name="Guest", age=20):
    print(f"Hello, 我是{name}! 今年{age}岁.")

greet()  # 使用默认值
greet("Bob", 25)  # 使用传入的实参
greet(age=30)  # 使用默认 name，但传入 age
# 默认参数可以和非默认参数混合使用，但默认值参数必须放最后
def greet(age, name="Guest"):
    print(f"Hello, 我是{name}! 今年{age}岁.")
greet(18)
def greet(name="Guest", age):  # 注意顺序
    print(f"Hello, 我是{name}! 今年{age}岁.")
greet(18)  # 如果上述代码改成这样就会报错
```

### 5.5 实参的类型

实参可以是任意的类型，也就是说形参里面的变量，可能会是一切东西

```python
def fn(a):
    print(a, type(a))
# 函数调用时不会限制你的类型，实参可以传递任意类型
fn(1)
fn(3.14)
fn(True)
fn(False)
fn('han')
fn([1, 2, 3])
fn((1, 2, 3))
fn({1, 2, 3})
fn({'1801': "小明", '1802': "小红"})
# 函数本身也能作为实参传递给形参,例如:
def fn():
    print("hello,world")
def fn2(a):  # a = fn
    a()  # fn()
fn2(fn)
# 又例如:
def fn(a, b):
    print(a)
    print(b)
def fn2(a):
    a(10, 20)
fn2(fn)
```

```python
# 1.编写一个函数，功能是输出hello,world

# 2.定义一个函数jia,传入两个参数num1,num2,输出它们的和'''
3.BMI是Body Mass Index 的缩写，BMI中文是“体质指数”的意思，是以你的身高体重计算出来的。BMI是世界公认的一种评定肥胖程度的分级方法，世界卫生组织(WHO)也以BMI来对肥胖或超重进行定义。
  身高体重指数这个概念，是由19世纪中期的比利时通才凯特勒最先提出。它的定义如下：
  体重指数(BMI)=体重(kg)÷身高^2(m)
  成人的BMI数值：
  过轻：低于18.5
  适中：18.5-25
  过重：25-30
  肥胖：30-35
  非常肥胖, 高于35
  专家指出最理想的体重指数是22。

    请你定义一个函数， 参数分别是 体重(kg单位) ,输入身高(m单位) 作为实际参数传入函数，计算出BMI 然后根据BMI 输出 过轻，适中，过重，肥胖，非常肥胖
'''
```

---

## 六、函数基础（下）

### 6.1 函数的参数

#### 6.1.1 可变参数(形参)★

可变参数，也称为不定长参数，允许函数接受可变数量的参数。在定义函数时，我们不需要明确指定每个参数的数量。Python 提供了两种主要的可变参数：`*args` 和 `**kwargs`。

6.1.1.1 *args

- 案例：求任意个数的和

```python
# 求2个数的和
def sum(a,b):
    print(a+b)
sum(10,22)
# 求3个数的和
def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)
会发现按照之前的写法，无法完成这个需求。因为形参是固定数量的，而实参也是固定数量的
无法做到想传入几个值，求几个值的和
可变参数：*
在定义函数写形参的时候可以在形参面前加一个 * 号 ，这样这个形参就可以获得我们所有的实参，将所有的实参都保存到一个元组中.

def fn(*args):
    print(args) # (1,2,3,4,5)
    print(type(args)) # tuple
fn(1,2,3,4,5)
# 会发现 当形参的前面加个*后，这个形参就可以接收任意的实参了，并包装为了一个元组
```

- *后面的形参，可以接收任意的位置实参，都会保存为一个元组，这个过程也可以叫装包

```python
# 求任意个数的和
def sum(*args): # 这里就可以直接传*参数，这样就不用写多个固定的了
    # 定义一个变量，来保存结果
    res = 0
    # 既然是一个元组，那就可以遍历
    for i in args:
        res += i
    print(res) # 最后res打印出来
# 传1个
sum(1) # 1
# 传2个
sum(1,2) # 3
# 传3个
sum(1,2,3) # 6
# 想传几个就传几个都会给加上，因为这是一个不定长的参数，这让开发变得更加的灵活
```

- 细节注意

```python
1.带 * 号的形参 只能有一个，因为1个就能够接收到所有的实参了，再多写一个接收不到没有意义
    # 这种会报错，因为args2根本收不到，都会被args1收走
    def f(*args1,*args2):
        pass

2.带 * 号的参数可以和其他参数配合使用，但是一般得写在最后面

def fn(a,b,*args): # 定义这么一个函数来打印a，b，c看看
    print('a =',a)
    print('b =',b)
    print('args =',args)
fn(1,2,3,4,5,6)
# args = (3, 4, 5, 6)

# *args如果放在最前面需要定义好关键字参数
def f(*args, b, c):
    print(args, b, c)
f(1,2,3,b=10,c=20) # 定义关键字参数

# 或者定义好形参的默认值,最终目的都是要让形参能够有值
def f(*args, b=10, c=20):  # 定义好默认值参数
    print(args, b, c)
f(1, 2, 3)
注：平时我们取带*参数的取名一般叫*args
```

6.1.1.2 **kwargs

*args有一个弊端就是只能接收位置参数

```python
def fn(*args):
    print("args =",args)
fn(1,2,3)
# 现在是可以接收任意的位置参数了
# 但是我现在想用关键字参数
fn(a=1,b=2,c=3)# 报错  *args只能接受位置参数# 怎么修改？
def fn(**kwargs):
    print("args =",kwargs) # {"a":1,"b":2,"c":3}字典
    print(type(kwargs)) # dict
fn(a=1,b=2,c=3)
```

可变参数总结

在 Python 中，可变参数使函数可以接受不定数量的参数，这大大提高了函数的灵活性。可变参数主要包括 `*args` 和`**kwargs`

- *args : 用于接收任意数量的位置参数，并将这些参数作为一个元组传递给函数。
- **kwargs: 用于接收任意数量的关键字参数，并将这些参数作为一个字典传递给函数。

#### 6.1.2 解包传参

指在函数调用时，将一个容器（如列表、元组、字典等）中的元素解开并传递给函数的参数。这可以通过 `*` 和 `**` 语法来实现。

```python
def fn(a,b,c):
    print("a =",a)
    print("b =",b)
    print("c =",c)

# 创建一个元组
t = (1,2,3)
# 现在假如想把元组里面的1，2，3分别作为参数传到函数去
fn(t[0],t[1],t[2]) # 注意可以ok，相当于 fn(1,2,3)# 但是如果元组特别庞大，就发现不好传递
# 简便方法：使用参数解包  fn(*t)
t = (1,2,3)
fn(*t) # 将元组解包为位置参数  效果等价于 fn(1,2,3)
t = [1,2,3]
fn(*t) # 当t改为列表一样适用，将列表解包为位置参数   效果等价于 fn(1,2,3)
# 当t为字典：
t = {"a":10,"b":20,"c":30}
fn(**t) # 将字典解包为关键字参数  等价于关键字传参
fn(a=10,b=20,c=30)
```

### 6.2 函数返回值

- 函数返回值通过`return`语句来实现
- 函数可以返回单一值，也可以返回多个值。
- 返回值类型可以是数字、字符串、列表、元组、字典等。
- 没有`return`语句时，函数返回`None`。

#### 示例1：返回数字

```python
def square(x):
    return x * x
result = square(4)
print(result)  # 输出: 16
result = square(4.5)
print(result)  # 输出: 20.25
```

- 在这个例子中，`square`函数返回输入数值的平方。

#### 示例2：返回字符串

```python
def greet(name):
    return f"Hello, {name}!"
message = greet("Alice")
print(message)  # 输出: Hello, Alice!
```

- `greet`函数返回一个格式化的字符串。

#### 示例3：返回多个值

```python
def stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total,average
a = stats([1, 2, 3, 4, 5])
print(a)  # stats函数返回一个元组，其中包含总和和平均值。(15, 3)
b, c = stats([1, 2, 3, 4, 5])
print(b)  # 输出: 15
print(c)  # 输出: 3.0
```

#### 示例4：返回列表

```python
def get_list(nums):
    list = [i for i in nums if i % 2 == 0] # 保留偶数
    return list
d = get_list([1, 2, 3, 4, 5, 6])  # d = [2,4,6]
print(d)  # 输出: [2, 4, 6]
```

- `get_list`函数返回一个包含偶数的列表。

#### 示例5：没有返回值

```python
def print_message(message):
    print(message)
result = print_message("This is a message!") #输出: This is a message!
print(result)  # 由于没有使用 return，输出: None
```

### 6.3 作用域和命名空间

回顾+梳理：回到最开始的 fn和fn()区别

```python
print(fn) # fn是函数对象，真实的表示函数本身
print(fn()) # 不表示函数本身，fn()在调用该函数，并最终会作为函数的返回值
fn()的一生：
1.执行fn内部的代码块
2.return，有则返回return后返回值，没有则默认返回None3.返回值传递给我们的函数调用处
```

#### 6.3.1 作用域★

程序中就是：指的是程序中变量、函数和对象等标识符可访问的区域

```python
# 比如
def my_function():
    x = 10  # 局部变量
    print(x)
my_function()  # 调用函数可以输出10
print("函数外部:",x)  # 报错
# 再比如
x = 10  # 全局变量
def my_function():
    print(x)
my_function() # 调用函数可以输出10
print("函数外部x:",x)
```

总结:函数内部定义的变量,外部无法访问，但是外部定义的变量，内外都可以访问

#### 6.3.2 全局作用域

函数以外的区域都是全局作用域

在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置被访问

```python
x = 10 # 全局变量x
def fn():
    print("函数内部x =",x)
fn()
print("函数外部x =",x)
```

![函数调用示意图](<D:/HP/Pictures/Saved Pictures/day 9函_p09-diagram.png>)

#### 6.3.3 函数作用域

函数内部就是函数作用域

在函数作用域里面定义的变量叫局部变量

- 生命周期:  存在的时间范围
- 全局作用域生命周期：程序运行时就有，程序结束才销毁
- 函数作用域生命周期：函数作用域是在函数调用时创建，在调用结束时销毁 (一次性用品)

```python
# 函数每次调用的时候会产生一个新的函数作用域
def fn():
    a = 10
    print("a =",a)
# 如果只是定义了这个函数 并没有函数作用域，里面的变量不会生效
fn() # 当调用的时候，程序中会创建函数作用域，当函数执行完毕返回，作用域消耗
fn() # 再调用一次，又会产生一个作用域
fn() # 再来一次，又是一个新的作用域
# 每调用一次就会产生一个函数作用域，我这里调用了3次就有3个函数作用域
举例
def func1():
    a = 10
    print("func1: a =", a)
def func2():
    a = 20
    print("func2: a =", a)
# 调用两个函数
func1()  # 输出: func1: a = 10
func2()  # 输出: func2: a = 20
也就是说每次函数调用的局部变量互不干扰。
```

- 关键点总结
- 1. 函数内部定义的变量为局部变量，这些变量仅在该函数的作用域内有效。2. 函数作用域的生命周期很短，从函数调用开始，到函数执行结束。3. 每次调用函数时，都会创建一个新的函数作用域。即使是同一个函数，每次调用产生的作用域也是完全独立的。4. 局部变量在函数作用域内生效，并且每次函数调用的局部变量互不干扰。
- 思考1 :内外变量都存在会输出什么?

```python
x = 10  # 全局变量
def my_function():
    x = 20 # 局部变量
    print(x)
my_function() # 补充:
print("函数外部x:",x)
```

- 思考2：函数嵌套

```python
def fn1():
    a = 30 # 函数内部定义一个a
    def fn2(): # fn1里面又定义一个函数fn2
        print(a) # a的值应该是？
    fn2()
fn1()

```

a值的寻找过程：

1. 先查看fn2函数作用域有没有a，没有则往外找fn12. 再查看fn1函数作用域有没有a，没有则往外找全局作用域3. 查看全局作用域有没有a，没有则报错

- 思考3：2个作用域fn2有关系吗？

```python
def fn1():
    def fn2():
        pass
def fn2():
    pass
```

- 答：没有关系，不会覆盖对方，都会有各自的变量作用域,它们各自定义的变量互不影响
- global和nonlocal
- global：可以将变量提域，可以在函数内部 声明全局变量，修改全局变量

```python
x = 10  # 这是一个全局变量
def test():
    global x  # 声明 x 是全局变量
    x = 20    # 修改全局变量 x
    print("x =", x)  # x = 20
test()
print("x =", x)  # x = 20
```

- nonlocal  （了解即可）
- 使用场景： 用于在嵌套函数内部声明一个变量为外层函数中的局部变量，从而允许在嵌套函数中修改该变量。 ·

```python
def f1():
    x = 10  # 外层函数的局部变量
    def f2():
        nonlocal x  # 声明 x 为外层函数的局部变量
        x = 20      # 修改外层函数的局部变量 x
        print("x =", x)  # 输出： x = 20
    f2()
    print("x =", x)  # 输出：x = 20
f1()
```

- 使用场景很少，了解即可

总结

1. 变量寻域规则：先看当前作用域，再一层一层往外找，直到全局作用域2. global：在函数内部声明全局变量3. nonlocal：嵌套函数的时候，用于内部函数修改外部函数变量

#### 6.3.4 命名空间

命名空间（Namespace）是一个映射（通常是一个字典），它将名字与对象关联起

来。作用是帮助管理变量名的作用域，避免命名冲突，并使得代码更加清晰易懂。

- locals() 内置函数可以查看当前作用域的命名空间字典
- globals()返回全局命名空间的字典

代码示例：

```python
x = 10  # 全局变量
def test():
    y = 20  # 局部变量
    print("locals():", locals())  # 查看当前作用域的命名空间
    print("globals():", globals())  # 查看全局命名空间

test()
```

```python
1.编写一个函数，功能是返回任意个数的和
  要求同时满足：  1.和的结果要用return表示
                2.用列表装任意个数,调用函数时实参需用解包传参

2.以下代码运行会输出什么？
def fn1():
    a = 30
    def fn2():
        a = 10
        print(a)
    fn2()
fn1()
```

---

## 七、函数进阶

### 7.1 高级用法

1.函数可以被引用(可以赋值)

```python
def fn():
    print("我是fn")

f = fn  # 注意是赋值函数本身，这个fn是指向内存地址,现在f的内存地址就和fn一样了
f()  # fn()
```

2.函数可以作为参数传入另外一个函数

```python
def fn():
    print("我是fn")

def fn2(x):
    x()

fn2(fn) # fn是一个函数，实参fn最终会传递给形参x
```

3.可以将函数作为返回值

```python
def fn():
    def inner():
        print('输出inner')
    return inner  # return 也可以返回任意类型，可以返回一个函数
fn()()
```

4.函数可以作为容器的元素

```python
def fn():
    print("我是fn")
list1 = [1, 2, 3, fn]  # 我们装入 1，2，3和函数fn
f = list1[3]
print(f)  # 得到一串地址
f()  # 其实就是fn()
```

### 7.2 匿名函数(lambda)

简单来说就是匿名，没有名字的函数，如果你只需要定义一个简单的函数，希望用一行实现，就可以使用lambda函数，它不需要显示定义名称，在高阶函数比较简单的时候可以使用

lambda函数的语法只包含一个语句，如下：

```python
lambda 形参:返回值
```

这个格式就是匿名函数的定义格式

```python
# 单参数：求平方
# 普通函数
def fn(x):
    return x * x  # 返回x * x
# lambda函数
lambda x: x * x
# 多个参数:求a+b+c
# 普通函数
def add(a, b, c):
    return a + b + c
# lambda函数
lambda a, b, c: a + b + c
```

- 定义了如何使用？

```python
f = lambda a, b, c: a + b + c
print(f(1, 2, 3))  # 6
不是匿名函数嘛？为什么还要取个名字。所以不推荐大家这么去写，这样写其实也并没有省事多少，匿名函数更多是作为参数使用。
```

- 总结lambda的目的是为了让某些情况代码简洁，效率和普通函数无区别lambda只适用于比较简单的函数lambda只适合一个函数只有一个返回值这种情况使用

### 7.3 高阶函数

#### 7.3.1 高阶函数简介

高阶函数：把函数作为参数传入的函数

先学习2个内置函数

- abs(x) : 返回x的绝对值
- 绝对值：将一个数变为正数【离0的距离】

```python
res = abs(-1)
print(res)  # 1
```

- round(x): 返回x的 四舍六入，小数五最后结果是偶数

```python
print(round(1.5))  # 2   小数点部位是5，最后结果是偶数
print(round(1.6))  # 2  小数点部位是6，直接入
print(round(2.5))  # 2  小数点部位是5，最后结果是偶数
print(round(2.6))  # 3  小数点部位是6，直接入
```

- 求2个数的绝对值处理后的和

```python
def ab_sum(a, b):
    return abs(a) + abs(b)
```

- 求2个数的四舍六入后的和

```python
def ab_sum(a, b):
    return round(a) + round(b)
```

- 体验高阶函数

```python
def ab_sum(a, b, f):
    return f(a) + f(b)
print(ab_sum(-1, -4.5, abs))  # 对绝对值求和
print(ab_sum(-1, -4.5, round))  # 对四舍六入求和
def xfs(a):
    return -a
print(ab_sum(-1, 2, xfs))  # 对相反数求和
print(ab_sum(-1, 2, lambda x: -x))  # 使用匿名函数
```

#### 7.3.2 map()★

map(函数,序列),将传入的 函数变量 作用到 序列变量 的每个元素中，并将结果组成新的迭代器返回。map 常用于统一修改序列，==返回一个新的序列==

案例1：将list1序列中各个数字的加1

```python
# 正常写法
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:  # 遍历list1
    list2.append(i + 1)  # 对i+1的结果放入list2
print(list2)
# map写法
# 自定义函数
def fn(x):  # 这个函数并不自由，必须要有1个形参x，这个x代表序列中的每个元素，会依次接受函数的洗礼
    return x + 1  # 返回值表示，元素最终修改值# 将fn作用到list1中的各个元素，结果需要再转为list查看
list2 = list(map(fn, list1))  # 等价于
[f(1),f(2),f(3),f(4),f(5)]
print(list2)
list2 = list(map(lambda x: x + 1, list1))  # 简洁版本
print(list2)
def xfs(x):
    return -x
print(list(map(xfs, list1)))  # 对list1求相反数
print(list(map(abs, list1)))  # 对list1求绝对值
def add1(x):
    return "漫天"
print(list(map(add1, list1)))  # list1中的元素全部都变成漫天了
```

- 总结
- 1. map高阶内置函数的作用是 操作序列中的所有元素，并返回的是一个迭代器，迭代器需要转成列表查看2. lambda函数非常适合配合高阶函数去做一些简单的需求，当作 函数参数来使用

#### 7.3.3 filter()★

filter(func,seq) 用于过滤序列，过滤掉不符合条件的元素。返回一个迭代器

案例2：保留一个序列中所有的偶数

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
# 先用以前的方法做一遍
for i in list1:
    if i % 2 == 0:  # 如果i % 2 == 0 说明i是一个偶数
        list2.append(i)
print(list2)  # 执行 ，这样就成功筛选出了所有的偶数。filter来做又有什么区别？
先学习它的参数函数
def 函数名(x): # 形参x，这个x代表序列中的每个元素，会依次接受函数的洗礼

    return True/False  # filter：表示当前元素是否保留的
                       # True保留 False过滤

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def o2s(x):
    if x % 2 == 0:  # 保留
        return True
    else:
        return False
print(list(filter(o2s, list1)))
# 简洁版
def o2s(x):
    return x % 2 == 0
print(list(filter(o2s, list1)))
print(list(filter(lambda x: x % 2 == 0, list1)))
 # 一行解决

# 知识补充
以前：0、空字符串去转bool结果是False
现在：0、空容器、None转Bool结果均是False
# 以下转bool全是False
字符串:''
整数: 0
小数: 0.0
列表:[]
元组:()
集合:set()
字典:{}
空类型:None
```

#### 7.3.4 sorted()★

以前学习过是排序，其实也可以传入一个函数作为参数，可以进行自定义排序

```python
list1 = [2, 4, 1, 3, 5, 6, 9, 7]
print(sorted(list1))  # 升序
print(sorted(list1, reverse=True))  # 降序
list1 = ["漫天:69", "翠果:79", "清越:89", "柠檬:100", "不晚:59"]
sorted1 = sorted(list1)
print(sorted1)  # 按照asc编码来排，不按照 59 69 79 89100
# 自定义排序规则
list1 = ["漫天:69", "翠果:79", "清越:89", "柠檬:100", "不晚:59"]
def f(x):  # x代表序列的每一个元素
    arr = x.split(":")  # split：按照指定的 分裂符进行裂开，裂开存储到列表中
    return int(arr[1])  # return 返回要排序的值
sorted1 = sorted(list1, key=f)  # 升序排
sorted1 = sorted(list1, reverse=True, key=f)  # 降序排
print(sorted1)
```

- 三个高阶内置函数的   函数参数的区别
- map(func,seq)
- func 返回值表示的 遍历过程中每个元素做出相应改变后的值filter(func,seq)
- func 返回值表示的 遍历过程中要保留的元素，T保留，F过滤sorted(seq,key=func)
- func 返回值表示的 遍历过程中要排序的值

### 7.4 递归函数（了解）

递归：解决一些重复逻辑性问题。

```python
有些实际问题，采用递归思想解决问题非常简单
```

所谓的递归就是函数自己调用自己

- 无限递归情况：会导致内存溢出，python会自动给报错，否则内存迟早崩溃

```python
def func():
    print("你好，我是漫天")
    func()
func()
```

- 递归需要满足的条件
- 1. 必须要有出口（某次调用，不再递归）2. 每次递归都得接近出口

利用递归思想，输出1~10

```python
def func(x):
    print(x)
    if x == 10:
        return
    func(x + 1)
func(1)
```

求阶乘，n! = n ×(n-1) × (n-2) × ...... 2 ×1     比如5！=5×4×3×2×1     特殊的有 `0! = 1`。

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

a = factorial(3)
print(a)
```

斐波那契数列

定义为 `F(0) = 0, F(1) = 1`，后续的数由前两个数的和得到：`F(n) = F(n`-`1) + F(n`-`2)`。

比如：0、1、1、2、3、5、8、13、21

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

fibonacci(4)
```

```python
# 1 . 使用 sorted() 函数将一个列表按元素的长度排序。
words = ["banana", "apple", "cherry",
"blueberry"]
结果应该是 ['apple', 'banana', 'cherry',
'blueberry']
# 2 . 用map来处理字符串列表,把列表中所有人名添加new_的前缀,比方new_lucy
name=['lucy','lilei','hanmeimei']
# 3 .使用filter内置函数，保留正数
# 需求：保留正数 ，过滤掉负数
list1 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]# 4 . 把字符串 "1 3 5 7 9" 转化为列表，并且列表元素均是整型
# tip: split + map
变化流程：'1 3 5 7 9' => ['1','3','5','7','9'] =>[1,3,5,7,9]
```

```python
# 1.哪些数据类型可以做 取下标、切片等操作？【答案3个】

# 2.让用户输入一个单词，并显示这个单词的长度

# 3.编写一个应用程序，计算并输出列表[9,1,3,5,6]中的最大值、最小值和平均值。

# 4.创建一个列表，包含以下五个水果："苹果", "香蕉", "橙子", "西瓜", "葡萄"。使用for循环遍历该列表，并依次打印 "我爱吃苹果","我爱吃香蕉" 等所有水果

# 5.编写一个应用程序，计算并输出列表[9,1,3,5,6]中的最大值、最小值和平均值。
注：如果不用内置函数如何实现求列表[9,1,3,5,6]的最大值、最小值、平均值呢？
```

---

## 八、序列类型（上）

### 内容

```python
-1 数据类型补充
-2 序列类型概念
-3 序列类型常用操作
```

### 8.1常见数据类型

```python
数值类型: 存储单个数据
    int 整型         6
    float 浮点型       6.6
    bool 布尔类型       True
序列类型: 存储多个数据
    list 列表
    tuple 元组
    str 字符串
总结: 根据使用场景不同所使用的数据类型不同,可以根据情况选择合适类型
```

### 8.2 序列简介

序列不是一个单独的python类型，它是一种数据结构，是对一类python数据类型进行了划分。

在 Python 语言中，通常将 字符串、列表 和 元组 归为序列类型。

序列主要特色1. 多种数据的集合序列不是单一的值，而是多个数据元素的有序集合。可以将序列理解为一个“容器”，它能够存储多个值，并且每个值的位置是有序的。

2. 支持下标操作

- 序列中的元素可以通过下标，又叫索引来访问容器中的某个元素。

本节课开始要接触3个序列的类型，分别是 列表、元组、字符串。他们直接都有共同的

操作，我们先从认识列表开始。

### 8.3 列表的创建(list)

列表的应用场景

- 思考：有一个人的姓名叫   '韩'  怎么写程序存储它的名字？

答：name = '韩'

- 思考：如果一个小队有5位成员，分别是：孙尚香、刘备、孙策、刘婵、周瑜，应该要怎么写程序存储？

答：

```python
name = ['孙尚香', '刘备', '孙策', '刘婵', '周瑜']
print(name)
```

语法

```python
[数据1,数据2,数据3]
```

列表可以一次性存储多个数据，且可以为不同的类型。数据数量没有限制

```python
teacher = ['漫天', '彬彬', '翠果', '七七']  # 一个存储老师的 列表
tools = ['98k', '三级头', 'uzi', '破军']  # 一个存储工具的 列表
other = [250, 3.1415926, True, "嘿嘿"]  # 4种类型都可以存
print(teacher)
print(tools)
print(other)
```

### 8.4 元组的创建(tuple)

英文名:tuple

元组基本和列表的作用一样，都是用来存储多个数据。

```python
number = (1, 2, 3, 4, 5)
print(number)
print(type(number))
# 括号可以直接省略，但是为了可读性，建议写上
number = 6, 7, 8, 9, 10
print(number)
# 如果元组里面只有1个元素，不可以这样
t = (6)
print(t, type(t))  # 6 , 'int'
# 因为()也有一个运算符的意思，所以会冲突，优先当作数学中的括号，单独表示需这样
t = (6,)
```

所有列表能做的事，元组都可以做，但也有所区别。

元组和列表主要区别：

- **列表是可以进行 增删改查**
- **元组不可以修改，只能查询**

### 8.5 序列的查询

列表list、元组tuple、字符串str都会有的特性

#### 8.5.1 下标

序列类型可以直接通过  下标（索引）来访问 某个元素

列表本质上是序列的类型。那么列表就会具有下标特色，下标可以像座位编号一样从列

表中找到对应的元素。

序列中的每个元素都有自己的下标(索引),从左往右下标从0开始

比如这样的一个列表

```python
# 从左到右下标默认是从0开始的，依次递增
arr = ['ok', 'yes', 'oh', 'no']  # 4个元素，4个字符串
# ok的下标是0
# yes的下标是1
# oh的下标是2
# no的下标是3
# 因此,只要有下标就可以提取列表中的某个元素
# 单个元素的访问: 列表[下标]  第i个元素的下标是i-1
print(arr[0])  # 'ok'
print(arr[1])  # 'yes'
print(arr[2])  # 'oh'
print(arr[3])  # 'no'
print(arr[4])  # 报错！ 注意，下标不可以超出最大值，如果列表有4个元素，最大下标就是3，所以最高只能是3
# 因为字符串和元组也是序列其实他们可以去用下标获取
s = "Python是世界上最好的语言"
print(s[0])
print(s[1])
print(s[2])
```

拓展：

```python
# 学了下标之后，已经知道怎么提取单个字符了，那如何提取最后一个元素？
s = "hello"
print(s[4])  # 这个很轻松，因为可以从左往右数到第5个，下标是4
# 这个该如何应对？
s = "https://www.baidu.com/s?ie=utf-
8&f=8&rsv_bp=1&tn=baidu&wd=漫天"
```

如果想取最后面的，从左往右不方便，此时可用反向下标

反向指的是从右往左，倒数第一个叫   -1，第二个就是    -2  ,

```python
# 取最后一个元素
s = "https://www.baidu.com/s?ie=utf-
8&f=8&rsv_bp=1&tn=baidu&wd=漫天"
print(s[-1])  # 表示右边第1个，"天"
```

想取中间元素怎么办呢？ 不急，后面会教

如果要一次性取多个元素怎么办？用切片

切片可以帮助我们从序列中提取一个子序列,数据类型不变

#### 8.5.2 切片

```python
arr = ["孙尚香", "刘备", "孙策", "刘婵", "周瑜"]# 使用切片
# 序列[开始下标:结束下标:步长=1]
# 这个规则和range函数非常相似，也是包头不包尾，步长默认为
1. 但是注意语法上的区别
bzr = arr[0:2]  # 从0开始，到2结束，包头不包尾，步长为1
print(bzr)  # ['孙尚香', '刘备']
print(type(bzr))
bar = arr[0:3]
print(bar)  # ['孙尚香', '刘备', '孙策']
# 简洁版
# 可以省略左边，默认从头开始切
bar = arr[:5]
# 省略右边，默认切到尾
bar = arr[0:]
# 完全一样的拷贝一份
bar = arr[:]
bar = arr[::2]
print(bar)  # ['孙尚香', '孙策', '周瑜']
bar = arr[::3]
print(bar)  # ['孙尚香', '刘婵']
# 当步长为负数的时候，从右边往左边看
# 经典应用：反转序列
bar = arr[::-1]  # 切片改为从右往左切，实现反转# 但不可以这样
bar = arr[0:5:-1]  # ?  []空列表，因为从0开始 ，步长为-1 是到不了4的
```

总结 ： 关于序列如何拿其中的元素

1. 单个拿

```python
序列[下标]  # 可以直接将其提取出来,里面是什么类型，拿出来就是什么
```

2. 多个拿

```python
# 可以拿多个，但是注意，拿出来的依然是和该类型相同的序列序列[开始下标:结束下标]
常见操作
# 反转
序列[::-1]
```

#### 8.5.3 成员运算符

| 运算符 | 描述                                                    | 实例                                              |
| ------ | ------------------------------------------------------- | ------------------------------------------------- |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

```python
# in：属于         not in：不属于
arr = ["孙尚香", "刘备", "孙策", "刘婵", "周瑜"]
print("孙尚香"  in arr)  # True
print("张飞" in arr)  # False
```

- 体验案例

```python
需求：输入账号判断是否已经注册,如果存在就让其循环重新输入,不存在就注册成功
name_list = ['root', 'admin', 'manager']
while True:
    name = input('请输入你的账号名：')
    if name in name_list:
        # 用户名存在
        print('用户名已经被注册，请重新输入')
    else:
        print('注册成功！')
        break
```

#### 8.5.4 序列遍历★

循环经常用来遍历序列遍历：将序列中的所有元素，依次1个1个访问到。 【全体获得】

```python
tools = ['斧头', '大宝剑', '长枪', '匕首', '太刀']# 遍历方法一 ： 利用下标来遍历序列
for i in range(0, len(tools)):  # len()作用：获取tools的长度,即5
    print(tools[i])
# 遍历方法二：
"""
for 变量名 in 序列:
    print(变量名)
"""
tools = ['斧头', '大宝剑', '长枪', '匕首', '太刀']
for i in tools:  # i 会直接获得列表里面的元素
    print(i)

总结：遍历就种2种
for i in range(len(序列)):
    print(序列[i])  # 优点：可以获得下标
for i in 序列:
    print(i)  # 优点是简洁

```

### 8.6 序列的运算

字符串它可以进行相加 和 乘法 ，其实序列类型都可以这样去做

序列的相加 就是 两边拼接

序列的相乘 就是 重复跟自己拼接

```python
s1 = "aa"
s2 = "bb"
list1 = [1, '2', 3]
list2 = ['4', 5, '6']
print(s1 + s2)  # 直接拼接 "aabb"
print(list1 + list2)  # 合并到一个列表  [1, '2', 3,'4', 5, '6']
print(s1 * 5)  # aaaaaaaaaa
print(list1 * 5)  # [1, '2', 3, 1, '2', 3, 1,'2', 3, 1, '2', 3, 1, '2', 3]
```

### 8.7 内置函数

内置函数是指已经在语言的标准库中定义好的函数，开发者可以直接使用

学习内置函数就要学习它的功能、参数、返回结果即可

- 所以如何学习一个函数？

```python
功能是什么
参数是什么
返回结果是什么
# 例：type()
功能：查看参数数据的数据类型
参数：被查看数据
返回：数据类型结果<class 'int'> <class 'str'><class 'float'> <class 'bool'>
# 例：print()
功能：将参数内容打印在屏幕上
参数：被输出数据
返回：无返回值
```

| 函数     | 功能                                                         |
| -------- | ------------------------------------------------------------ |
| len()    | 计算序列的长度，即返回序列中包含多少个元素。                 |
| max()    | 找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。 |
| min()    | 找出序列中的最小元素。                                       |
| sum()    | 计算元素和。                                                 |
| sorted() | 对元素进行排序。                                             |

8.5.5.1 len()

len() : 计算序列的长度，即返回序列中包含多少个元素。

```python
s = "hello,world"
print(len(s))  # 11
lis = [6, 6, 6, 6, 7]
print(len(lis))  # 5
```

8.5.5.2 max()和min()

max() 方法返回给定参数的最大值，参数可以为序列。

```python
x = max(80, 100, 1000)  # 返回最大的数字
print(x)
x = max([80, 100, 1000])
print(x)
print(max("abcdzefg"))  # 通过编码返回最大字符
print(max("ab", "ac"))  # 比较原则是先比较 第一个字符，如果第一个字符相等，再比较第二个字符，以此类推，所以最后当然是ac
min的效果和max一模一样，取最小值
```

8.5.5.3 ASCII编码

- ASCII ((American Standard Code for InformationInterchange): 美国信息交换标准代码）是基于拉丁字母的一套电脑编码系统，主要用于显示现代英语和其他西欧语言。它是最通用的信息交换标准，并等同于国际标准ISO/IEC646。ASCII第一次以规范标准的类型发表是在1967年，最后一次更新则是在1986年，到目前为止共定义了128个字符。 计算机的本质是处理二进制数据，即 0 和 1 的序列。为了让计算机能够理解和处理文字、符号等字符，人们设计了字符编码系统，将字符映射到唯一的数字。ASCII（American StandardCode for Information Interchange，美国信息交换标准代码）就是这样一种早期的编码系统。

举例：摩斯电码，这些编码的目的就是把字符转成数值信号

![摩斯电码表](<D:/HP/Pictures/Saved Pictures/day 05_p13-diagram.png>)

计算机的ASCII码也是同理，把所有字符编码写成数字形式a -> 97-> (0110 0001)

我们不需要掌握ASCII码，只需要理解一切皆可转二进制

```python

# ord() 函数，以一个字符串作为参数 返回对应的 ASCII 数值
print(ord("b"))  # 98
# chr() 用一个整数作参数，返回一个对应的字符。
print(chr(99))  # 'c'
```

![ASCII 字符代码表](<D:/HP/Pictures/Saved Pictures/day 05_p14-diagram.png>)

8.5.5.4 sum()

sum() : 对序列进行求和计算。

```python
arr = [1, 5, 2, 4, 3]
print(sum(arr))  # 求和
```

8.5.5.5 sorted()★sorted 可以对序列类型进行排序操作,最终会得到一个==新的列表==，原列表不会变。

```python
arr = [1, 5, 2, 4, 3]
print(sorted(arr))  # 升序,从小到大
print(sorted(arr, reverse=False))  # 升序,从小到大
print(sorted(arr, reverse=True))  # 降序,从大到小
print(sorted(arr)[::-1])
# [5,4,3,2,1]
print(sorted("badc"))  # ['a', 'b', 'c', 'd']  按ASCII编码排序
print(sorted((5, 2, 6, 1)))  # 元组也可以排序,最终得到一个列表
```

```python
# 1.哪些数据类型可以做 取下标、切片等操作？【答案3个】

# 2.让用户输入一个单词，并显示这个单词的长度
# 3.编写一个应用程序，计算并输出列表[9,1,3,5,6]中的最大值、最小值和平均值。
# 4.创建一个列表，包含以下五个水果："苹果", "香蕉", "橙子", "西瓜", "葡萄"。使用for循环遍历该列表，并依次打印 "我爱吃苹果","我爱吃香蕉" 等所有水果
# 5.编写一个应用程序，计算并输出列表[9,1,3,5,6]中的最大值、最小值和平均值。
注：如果不用内置函数如何实现求列表[9,1,3,5,6]的最大值、最小值、平均值呢？
```

---

## 九、序列类型（下）

复习：

```python
序列上
属于序列：list、tuple、str  序列共有特色  有序容器
        1.拥有下标去 单独访问元素
            正向：从左到右0开始
            反向：从右到左-1开始
        2.切片：群体访问
            序列[开始下标:结束下标:step]
        3.序列遍历 for i in 序列：  print(i)
        4.运算符 in   not in     结果bool
        5.共有函数
            max()  # 求最大值
            min()  # 求最小值
            sum()  # 求和
            sorted(变量名,reverse = False)  # 排序
            len()  # 求元素的数量
```

### 9.1 列表常用方法

- 什么是方法？

方法其实和函数很像，可以理解为也是一种功能。但是函数和方法也有区别

```python
函数，独立的功能，可以在程序的任何地方调用。
    print()
    type()
    len()
    sum()
    max()
    min()
    ....
方法,必须绑定某个对象来用,表示某对象专属的函数
    格式通常是 对象.方法()
    列表方法：[1, 2, 3].append(4)，向列表中添加元素。
    字符串方法："hello".upper()，将字符串转换为大写。
```

#### 9.1.1 增

- append(): 添加一个数据，添加到列表的最后一位

```python
# 语法
列表.append(数据)
li = [2, 3, 4, 6, 8, 9, 10]
# 方法使用,必须通过 .
li.append(6)  # 尾部添加6
print(li)  # [2, 3, 4, 6, 8, 9, 10, 6]li.append(66)  # 尾部添加66
print(li)  # [2, 3, 4, 6, 8, 9, 10, 6, 66]
```

- insert() : 添加一个数据，添加到指定下标位置

```python
# 语法
列表.insert(下标, 数据)
li = [2, 3, 4, 6, 8, 9, 10, 6, 66]
li.insert(0, "nice")  # 下标0处添加 'nice'
print(li)  # ["nice", 2, 3, 4, 6, 8, 9, 10, 6,66]
li.insert(2, "python")  # 下标2处添加 'python'
print(li)  # ["nice", 2, "python", 3, 4, 6, 8,9, 10, 6, 66]
```

- extend() : 延长序列

```python
li = [1, 2, 3]
li.extend([4, 5, 6])
print(li)  # [1, 2, 3, 4, 5, 6]
```

#### 9.1.2 删

- pop():根据下标删除元素，如果不填默认删最后

```python
li = [1, 2, 3]
li.pop(1)  # 删除下标为1的值
print(li)  # [1, 3]
```

- remove(): 根据值删除元素，若有多个，删除第一个值

```python
li = [1, 2, 3, "哈哈", '呵呵', "哈哈"]
li.remove("哈哈")  # 删除"哈哈"
print(li)  # [1, 2, 3, '呵呵', '哈哈']
```

- clear():清空列表里面所有的数据

```python
li = [1, 2, 3, "哈哈", '呵呵', "哈哈"]
li.clear()  # 清空列表
print(li)  # []
```

+ del(和pop差不多，只是del没有返回值，并且del还可以批量删除)

	```python
	mylist = ["han","shang","qin"]
	del mylist[2]
	print(mylist) #输出['han','shang']
	
	mylist = ["han","shang","qin"]
	del mylist[0:1]  #切片：左闭有右开
	print(mylist)    #输出：["shang","qin"]
	
	mylist = [1,2,3,4,5]
	del mylist[0:4:2]  #[左值，右值，步长]
	print(mylist)    #输出:[2,4,5]
	```

####  9.1.3 改

```python
1.单个修改: 直接通过下标进行赋值修改
例如：
li = [1, 2, 3]
li[0] = 6  # 下标0处改成了6
print(li)  # [6, 2, 3]
2.多个修改: 通过切片方式进行修改
例如：
li = [1, 2, 3]
li[1:3] = ["码途",'钥匙']
print(li)  # [1, '码途', '钥匙']
```

#### 9.1.4 查

```python
查:
    1.index: 根据内容获取指定数据的下标，找不到则报错
    2.count: 可指定一个元素，统计在列表的数量

例如：
number = [60, 70, 50, 80, 99]
print(number.index(70))  # 1
print(number.count(60))  # 1
```

#### 9.1.5 其他

有些方法会有特别的处理功能

```python
# sort() 排序,让列表的内容按照降序/升序的方式来排序
li = [1, 9, 2, 8, 3, 7, 4, 6, 5]
li.sort()  # 直接将列表改为升序
print(li)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
li.sort(reverse=True)  # 改为降序
print(li)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# sort()与sorted(arr)区别:
li = [1, 9, 2, 8, 3, 7, 4, 6, 5]
lst = sorted(li)  # sorted()会得到一个新的列表
print(li)  # li还是原来的li
print(lst)
li.sort()  # li改为升序
print(li)
```

### 9.2 元组常用方法

#### 9.2.1 查

元组的内容是不可变的.所以它只有查询方法,并且跟列表的用法同理

```python
# index()方法举例:
my_tuple = (1, 2, 3, 4, 5)
index = my_tuple.index(3)
print(index)  # 输出: 2
# count()方法举例：
my_tuple = (1, 2, 3, 4, 5, 3)
count = my_tuple.count(3)
print(count)  # 输出: 2
```

### 9.3 可变与不可变类型

数字、字符串、元组 是不可变类型

列表、字典 、集合 是可变的

```python
a = (1, 9, 2, 8, 3, 7, 4, 6, 5)  # 元组是不能改的..# 利用赋值去修改元组
a[0] = 10  # 直接error报错
```

### 9.4 字符串常用方法

#### 9.4.1 find()

作用：可指定范围查找字符串，返回其下标的值，如果找不到返回-1语法

```python
str.find(s)
 - 需要查找的字串
例如：
s = "hello"
print(s.find("a", 2, 4))  # -1
print(s.find("o"))  # 4
"""
    如果需要指定范围去找
    str.find(s,开头范围，结束范围)  包头不包尾"""
```

#### 9.4.2 index()

作用：可指定范围查找子串，返回索引值，找不到就报错

语法:

```python
str.index(str, start=0, end=len(string))
```

- str -- 指定检索的字符串
- start -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。（包头不包尾）

该方法与  find()方法一样，只不过如果str不在 string中会报一个异常。而find是返回-1

```python
s = "hello,world,python,php"
print(s.index("o"))  # 4
print(s.index("h"))  # 0
print(s.index("h", 1))  # 从下标1开始找,输出15
print(s.index("@"))  # 报错
```

#### 9.4.3 count()

count() 方法:返回找到的子串个数

```python
s = "hello,world,python,php"
print(s.count("h")) # h的出现次数 3
```

#### 9.4.4 lower和upper()

```python
# lower()  :转小写
# upper()  :转大写
s = "hello,world,python,php"
s2 = s.upper()
print(s2)
s3 = s2.lower()
print(s3)
while True:
    word = input("请输入单词(输入q/Q则退出)：")
    if word.upper() == 'Q':  # if word in['q','Q']:
        print("退出成功，欢迎下次再来！")
        break  # 退出循环
    print(len(word))
```

#### 9.4.5 split() ★

split() : 切分字符串，将 字符串 转 列表，默认以空格切分，也可以指定字符切分

项目多用 常用将一个有分隔符的字符串转为列表操作

```python
# split 作用：按照指定切割符，去将字符串转成列表,通常需要赋值，原字符串并不改变
s = "hello world python nice"
# 默认以空格切分 ['hello', 'world', 'python','nice']
print(s.split())
s = "java,c++,c#,js,python,php,scala"
# 按逗号切分 ['java', 'c++', 'c#', 'js', 'python','php', 'scala']
print(s.split(","))
# 思考题：如何将多行字符串转列表？
s = '''张三
李四
王五
赵六'''
student = s.split('\n')  # 按换行切分
print(student)
```

#### 9.4.6 replace() ★

replace():把字符串中的 子串 替换成 新字符串str.replace(old, new , count)

old：要替换的字符串

new：新的字符串

count：替换次数 (默认所有)

```python
s = "hello,world,python,php"
print(s.replace("h", "ha"))
print(s.replace("h", "好", 1))  # 替换一次   好ello,world,python,php
print(s.replace("h", "好", 3))  # 替换三次   好ello,world,pyt好on,p好p
# 场景：清除不要的数据 ,空字符串表示去除
print(s.replace("hello", ""))
```

#### 9.4.7 join() ★

join(): 用于将序列中的元素以指定字符串连接生成一个新的字符串

join()常用于将列表类型转为字符串

```python
s = "hello world python nice"
list_word = s.split(" ")
print(list_word)  # ['hello', 'world', 'python','nice']
# join以当前字符串作为连接符，将列表中的所有元素，合并成一个字符串
# 用换行把['hello', 'world', 'python', 'nice']各个元素连接
print("\n".join(list_word))
# 用空格连接['hello', 'world', 'python', 'nice']各个元素
print(" ".join(list_word))
# 思考：不用join该如何连接？
lis = ['hello', 'world', 'python', 'nice']# 法1：
str1 = ''
for i in lis:
    str1 += i
print(str1)
# 法2：
for i in lis:
    print(i, end=' ')

```

#### 9.4.8 strip()

去除前后的空白

```python
# strip() 前后去空
s = "        123        "
print(s.strip())  # "123"
user = input('请输入账号：').strip()  # 清空前后的空白
if user == 'root':
    print('成功')
else:
    print('不成功')
```

更多的方法可以访问别人的一个博客

https://www.cnblogs.com/fyknight/p/7895894.html

了解即可，更多情况 查询使用

### 9.5 列表推导式★

灵活快速创建列表的方式，功能很强大。

列表推导式又叫列表生成式。

- 创建列表三种方法:

```python
# 老方法
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
# 法2:   range() 是内置函数，返回一个不可变的序列，这里会生成从 1 开始到 9 结束的整数序列
list2 = list(range(1, 10))
print(list2)
# 法3:  列表推导式
list3 = [i for i in range(1, 10)]
print(list3)
# 语法：将for循环变量名i的值添加到列表中
# 列表推导式的本质
b = []
for i in range(1, 10):
    b.append(i)
print(b)
list3 = [i * i for i in range(1, 10)]
print(list3)  # 将for循环变量名i的平方添加到列表中# 建一个包含1-10内的所有偶数的列表
s = [i for i in range(1, 11) if i % 2 == 0]
print(s)
```

### 9.6 序列嵌套

```python
# 序列：str list tuple 元组与列表可以直接嵌套,字符串不能直接嵌套字符串
# 以二维列表为例：
lis2 = [
    [10, 20, 30, 40, 50],
    [50, 30, 20, 10, 60],
    [70, 90, 100, 99, 98]
]
for i in lis2:
    print(i)  # 元素依旧还是列表
print(len(lis2))  # 二维列表的长度
# 二维列表的一次提取依旧是一个列表
print(lis2[0])
print(lis2[1])
print(lis2[2])
# 访问第一个列表的第一个元素
print(lis2[0][0])
# 访问第三个列表的第三个元素
print(lis2[2][2])
```

```python
1.创建一个列表，包含以下五个水果："苹果", "香蕉", "橙子","西瓜", "葡萄"。
    1) 向列表末尾添加 "草莓"。
    2) 在 "橙子" 和 "西瓜" 之间插入 "芒果"。 insert(下标，内容)
    3) 删除 "香蕉"。 pop  remove
    4) 使用切片操作，获取 "橙子" 到 "葡萄" 的子列表。2.input输入一个包含多个单词的字符串，例如 "Python is a powerful language"。
编写代码将该字符串按 空格 分割为列表，并遍历该列表打印每个单词
```

---

## 十、散列类型

### 10.1 散列类型(哈希类型)

数据类型，大类分为：

1.数值类型： int , float , bool  --> 存储一个数值

2.序列类型： str , list , tuple --> 存储多个数据的 有序容器

3. 散列类型：set、dict，通过哈希组织数据，不能像序列一样用连续整数下标访问

- 散列类型的特点？
- 集合无序且内部元素不重复；字典用键访问值。

有序一般是指有下标这种概念，而无序则没有下标。

无序则意味着数据元素的排列没有明确的顺序，不能通过下标来直接访问。

在这种情况下，可以通过遍历来查找某个元素，也可以转列表用下标查询。

### 10.2 集合(set)

#### 10.2.1 概念

集合是一种无序的、可变的、不包含重复元素的数据结构。可用来去重和逻辑判断生活中哪些东西无法重复？比如身份证、学号

类似于身份证、学号这种(不重复)的数据，可以考虑使用集合来定义

#### 10.2.2 性质

- 唯一性：集合中的数据是唯一的，不可以重复
- 可变性：和列表一样，是可变类型，存在可以直接增加和删除的方法
- 无序性：没有下标，因此集合无法像列表字符串元组那样用下标访问内部元素

```python
# 创建语法
集合名 = {数据1,数据2,数据3,数据4...} # 如果有重复数据，会自动去除
set1 = {1,2,3,4,1,2,6,5,7,7,7,9,8,2,8}
print(set1) # 正常输出一个集合，里面的数据默认去重
print(type(set1))  # 查看类型 set
print(set1[1]) # 散列类型无序，不可以通过下标提取元素，报错
推导式:集合推导式与列表推导式相似
# 创建一个集合，包含1到10的平方数
squares = {x**2 for x in range(1, 11)}
print(squares)
# 创建一个空集合
set1 = {}  # 经典错误，这是空字典
# 创建空集合应该这样操作
set1 = set()
注意：创建空集合的时候必须使用set()而不能时候{},因为{}默认是空字典
空数据类型汇总：
li1 = [] #空列表
tu1 = () # 空元组
    # 元组里面单个元素的表示
    # (1,) (1)
str1 = "" # 空字符串
dict1 = {} # 空字典
set1 = set() # 空集合

# 去除重复元素
number = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8,8, 9, 10]
print(list(set(number)))  # 先转集合(去重),再转回列表# 用以前所学知识怎么处理？
number = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8,8, 9, 10]
new_number = []  # 定义一个空列表用来辅助去重
for i in number:
    if i not in new_number:
        new_number.append(i)
print(new_number)
print(number)
```

#### 10.2.3 集合运算符

| 运算操作 | Python运算符 | 含义                           |
| -------- | ------------ | ------------------------------ |
| 交集     | &            | 取两集合公共的元素             |
| 并集     | \|           | 取两个集合中的全部不同元素     |
| 差集     | -            | 取一个集合中另一集合没有的元素 |

```python
集合可以进行逻辑判断
集合1 & 集合2 --> 判断交集
集合2 | 集合1 --> 判断并集
集合1 - 集合2 --> 判断差集
交集：两个集合里面共同有的数据
并集：两个集合里面的全部数据
差集：集合1 - 集合2 减去交集，剩下的就是差集
# & 交集，取两个集合的公共元素
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2) # 获得公共部分 {3}
# | 并集，取两个集合的全部元素,
print(set1 | set2) # 获得并集 {1,2,3,4,5}

# - 差集，取一个集合中另一个集合没有的元素 将set1中的属于set2的元素删除
print(set1 - set2) # 获取差集 {1,2}
注意，集合内部元素必须是不可变类型(整数、字符串、元组等),但集合本身是可变类型
集合的作用：
    1.存储非重复数据
    2.用于将序列类型去重，逻辑判断（交集，并集，差集）
```

#### 10.2.4 方法

- 增
- add()：参数为要添加的对象，集合不保证元素排列顺序

```python
s = {"星期一"}
s.add("星期二")
print(s)
s.add("星期三")
print(s)
```

- update()：参数为容器类型，会遍历其中的元素并加入集合

```python
s.update("123")   # 字符串中的每个字符都会被加入集合
print(s)
s.update([4,5,6]) # 列表中的 4、5、6 会被依次加入集合
print(s)
```

- 删
- pop()：删除并返回集合中的一个任意元素

```python
s = {'python','java','php','c'}
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
```

- remove()：按值删除，参数为要删除的元素，如果元素不存在报错

```python
s = {'python','java','c'}
s.remove('python')
print(s)
s.remove('java')
print(s)
s.remove('c')
print(s)  # set() 空集合
```

- discard()：同remove，元素不存在也不会报错

```python
s.discard('python')
print(s)
s.discard('java')
print(s)
s.discard('c')
print(s)
```

- clear()：清空集合中的元素

```python
s.clear()
print(s)
```

+ 其他：

	+ difference:  告诉我差集是什么,返回新集合，不修改原集合

		```python
		set_1 = {1,2,3}
		set_2 = {2,3}
		set_3 = set_1.difference(set_2)
		print(set_3) #{1}
		```

	+ difference_update(): 在集合1中，删除集合2中存在的元素，集合1被修改，集合2不变

		```python
		set_1 = {1,2,3}
		set_2 = {1,2}
		set_1.difference_update(set_2)
		print(set_1)
		```

	+ union(): 得到一个新集合，内含2个集合的全部元素，原有的2个集合内容不变

		```python
		set_1 = {1,2,3}
		set_2 = {1,2,0}
		set_3 = set_1.union(set_2)
		print(set_3)
		```

	+ len(): 求集合的长度

		```
		set_1 = {1,2}
		set_2 = {1,2,3}
		print(len(set_1))
		print(len(set_2))
		```

| 方法                                 | 参数数量   | 参数类型           | 是否修改原集合 |
| ------------------------------------ | ---------- | ------------------ | -------------- |
| `add(x)`                             | 1 个       | 一个可哈希元素     | 是             |
| `update(*others)`                    | 0 个或多个 | 每个都是可迭代对象 | 是             |
| `remove(x)`                          | 1 个       | 一个可哈希元素     | 是             |
| `discard(x)`                         | 1 个       | 一个可哈希元素     | 是             |
| `pop()`                              | 0 个       | 没有参数           | 是             |
| `clear()`                            | 0 个       | 没有参数           | 是             |
| `union(*others)`                     | 0 个或多个 | 可迭代对象         | 否，返回新集合 |
| `difference(*others)`                | 0 个或多个 | 可迭代对象         | 否，返回新集合 |
| `difference_update(*others)`         | 0 个或多个 | 可迭代对象         | 是             |
| `intersection(*others)`              | 0 个或多个 | 可迭代对象         | 否，返回新集合 |
| `intersection_update(*others)`       | 0 个或多个 | 可迭代对象         | 是             |
| `symmetric_difference(other)`        | 1 个       | 一个可迭代对象     | 否，返回新集合 |
| `symmetric_difference_update(other)` | 1 个       | 一个可迭代对象     | 是             |

###  10.3 字典(dict)

具备查询功能

#### 10.3.1 概念

`dict`（字典）是一种内置的数据类型，包含键值对（key-valuepairs）。

key指的是字典中的每个元素的标识符，用于唯一标识每个存储的值。

字典的每个元素都是由一个键和一个对应的值组成的。键必须唯一且可哈希，例如数字、字符串以及内部元素都可哈希的元组；值可以是任何数据类型。

```python
字典就是以为键值对来存储的
键值对语法: key : value
字典的表现形式：字典和集合一样也是用大括号，不过大括号里面存储的是键值对（说明关系的数据），那么它就是字典。
语法格式：
    字典名 = {键名1:值,键名2:值,....}

如何查字典？
    字典名[键] # 可以查询出值

name = {
    "1801":'小明',
    "1802":'小红',
    "1803":'小黑'
}
print(name,type(name))
print(name["1801"]) # 通过 key 去查询 value
print(name["1802"]) # 通过 key 去查询 value# 英汉词典举例
word_dict = {"hello": "你好",'world':'世界'}
print(word_dict,type(word_dict))
print(word_dict["hello"]) # 通过 key 去查询 value推导式创建
# 创建一个字典，键是1到5的数字，值是键的平方
squares = {x : x**2 for x in range(1, 6)}
print(squares)  # 输出: {1: 1, 2: 4, 3: 9, 4: 16,5: 25}
# 思考：以下print会输出什么内容？
user_card = {
    '姓名': '小黑',
    '年龄': 18,
    '工作': '忍者',
    '家乡': '忍村',
    '电话': 10087
}
# 通过 键key 访问 值value
print(user_card['姓名'])
print(user_card['年龄'])
print(user_card['工作'])
```

#### 10.3.2 性质

```python
1. 字典不能通过整数下标访问，但可以通过键查询值；Python 3.7 及以后会保留键的插入顺序
    字典名[键]
2.不重复，字典的键，是不可以重复的
# 实在没办法，键重复了，那就取最后一个键值对
dict1 = {"a":1,"b":2,"a":3,"a":4,"a":5,"a":0}
print(dict1) # {'a': 0, 'b': 2}
3.可变性，字典里面的数据是可变的，而且可以嵌套
# 修改值直接用键赋值
dict1 = {"a":1,"b":2}
print(dict1) # {'a': 1, 'b': 2}
dict1["a"] = 100
print(dict1) # {'a': 100, 'b': 2}
# 字典嵌套
person = {
    "名字": "Alice",
    "年龄": 30,
    "地址": {
        "街道": "123 Main St",
        "城市": "Wonderland",
        "邮编": "12345"
    },
    "联系方式": {
        "电话": "123-456-7890",
        "邮箱": "alice@example.com"
    }
}
print(person["地址"])
print(person["地址"]['邮编'])
print(person["联系方式"])
print(person["联系方式"]['电话'])
```

#### 10.3.3 方法

- 增
- 不用方法，直接赋值

```python
zd = {"a":1,"b":2}
# 直接赋值即可
zd['c'] = 3 # 相当于添加了一个键值对  "c":3
print(zd)
```

- 删
- pop:删除指定的键值对

```python
zd = {"a": 1, "b": 2}
print(zd)
# 删除, 根据键来删除  键值对
zd.pop("a")
print(zd)
zd.pop("b")
print(zd)
```

- clear:清空字典

```python
字典名.clear
nr.clear() --> 输出一个空字典{}
```

- 改
- 直接赋值

```python
zd = {"a":1,"b":2}
print(zd['b'])
zd["b"] = 3 # 直接这样能修改
print(zd) # {"a":1,"b":3}
# 也可批量改
zd.update({'a':3,'b':4})
print(zd)
# 或者批量新增
zd.update({'c':3,'d':4})
print(zd)
```

- 查
- 最简单的方法

```python
zd = {"a": 1, "b": 2}
# 直接通过key查询
print(zd['a']) # 1
print(zd['b']) # 2
```

- keys():获得所有的键

```python
字典名.keys()
# 获得字典的所有的键,生成一个伪列表类型,支持for循环遍历,但不支持下标访问
zd = {"a": 1, "b": 2}
print(zd.keys())  # dict_keys(['a', 'b'])# 试试遍历zd.keys()会有什么效果？
for key in zd.keys():
    print(key)

# 转列表后可以用下标访问元素
print(list(zd.keys())[0])
```

- values():获取所有的值

```python
字典名.values()
# 获得字典的所有的值,生成一个伪列表类型,用法同keys()
zd = {"a": 1, "b": 2}
print(zd.values())
# 遍历
for value in zd.values():
    print(value)

# 转列表后可以用下标访问元素
print(list(zd.values())[0])
```

- items():获取所有的键值对

```python
字典名.items()
zd = {"a": 1, "b": 2}
print(zd.items())  #  dict_items([('a', 1),('b', 2)])  伪列表类型

# 字典如何遍历？
# 方法一
for i,j in zd.items():
    print(i,j)  # i是键名,j是值

# 方法二
for key in zd.keys():
    print(key, zd[key])  # 遍历所有的键值对
```

==一定要记得字典集合都是是无下标，不可重复的，可修改的特性==

```python
# 1.将列表数据[1,2,3,2,1,4,4,4,2,5,6,7,7,9,8,10,10]去重
lis = [1,2,3,2,1,4,4,4,2,5,6,7,7,9,8,10,10]# 2.有字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能：
    (1)、添加一个键值对"k4"："v4",输出添加后的字典 dic

    (2)、请修改字典中 键"k1" 对应的值为 "python" ,输出修改后的字典dic

    (3)、遍历字典 dic 中所有的key
    (4)、同时遍历字典 dic 中所有的key和value

    (5)、删除字典 dic 中的键值对"k2","v2",并输出删除后的字典 dic

    (6)、单独查询字典 dic 中“k1”对应的值

# 判断题：以下对象能否作为 set 元素或 dict 的键，也就是是否可哈希？
# 可哈希：可以计算相对稳定的哈希值，并能用于集合和字典键
1. (1, 3, 5)  # 元组是不可变类型,可哈希
2. (1, [2, 3])  # 内部包含了列表,而列表可变,不可哈希
3. "python"  # 字符串永远可以哈希
4. ({1}, 2)  # 内部有集合set,而set不可以哈希
```