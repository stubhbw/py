# _Python笔记_

## 1. 文件类型
###.py
* 最常见的类型
###.pyc
* 该类型是.py文件编译后的二进制文件,运行效率当然比.py文件快啦
* 编译的命令行如下:

		python -O-m py_compile hello.py
###.pyo
* 经过优化编译的原文件,这个比.pyc效率更高
## 2. 变量
### 命名规则:
* 变量可以是数字,字母,下划线组合,不能以数字开头
### 简单理解:
* Python中的变量类似是一个标签,贴向内存地址中的值,变量的重新赋值类似于标签移动

## 3. 运算符和表达式

###  赋值运算符

		= 等于,赋值
		+= 加等
		-= 减等
		*= 乘等
		/= 除等
		% 求余等
###  算术运算符

		+ 加
		- 减
		* 乘
		/ 除
		// 整除法
		% 求余数
		/** 幂  例如:  3**2 表示3的2平方为9
###  关系运算符

		<
		>
		<=
		>=
		!=
		==
###  逻辑运算符
	
		and 逻辑与
		or 逻辑或
		not 逻辑非
### 表达式概念
* 将不同的数据(包括变量,函数)用运算符用一定的规则连接起来的一种式子

## 4. 数据类型 (大部分计算机编程语言都有的定义,用一个盒子或者说空间把数据装起来)
###  整型 int

		a = 123
		# type() 调用该函数可得到变量的数据类型
		print(type(a))
	
		输出:
		<type 'int'>
###  长整型 long

		b = 999999999999999999999
		print(type(b))
		c = 99L
		print(type(c))
		输出:
		<type 'long'>
		<type 'long'>
###  浮点型 float

		d = 13.0
		print(type(d))
		e = 5.0 / 2
		print(type(e))
	
		输出:
		<type 'float'>
		<type 'float'>
###  复数类型 complex

		f = 3.14j
		print(type(f))
	
		输出
		<type 'complex'>
###  字符串 str  (序列类型数据)

* 定义:

		# ----单引号 ''
		str1 = 'hello world'

		# ----双引号 ""
		str2 = "hello world"

		# ----注意嵌套使用,转义字符
		str3 = "hello i'm hebw"
		str4 = "hello i'm \"hebw\""

		# ----三引号 """""" 可用于保存文字的格式,如下str5等同于str6
		str5 = """Tom:
	    i'm hebw,nice to see you
	    ok , see you again."""
		str6 = "Tom:\n\ti'm hebw,nice to see you\n\tok , see you again."

* 常用操作:

		# 占位符的使用
		def p(x, y):
    		print("%s : %s" % (x, y))
		p(1, 2)
		p(*t)

		输出:
		1 : 2

		# capitalize() 首字母大写
		str = 'aaabcde,fghijklmn,opqrst,uvwxyz'
		print(str.capitalize())

		输出:
		Aabcde,fghijklmn,opqrst,uvwxyz
		
		# replace() 替换
		str = 'aabcde,fghijklmn,opqrst,uvwxyz'
		print(str.replace('a', 'Hello_A'))
		print(str.replace('a', 'Hello_A', 2))
		
		输出:

	Hello_AHello_AHello_Abcde,fghijklmn,opqrst,uvwxyz
		Hello_AHello_Aabcde,fghijklmn,opqrst,uvwxyz

		# split() 切割,按照某元素切割,返回一个列表,第三个参数表示切割的次数,默认全部
		print(str.split(','))
		ip = '192.168.0.1'
		print(ip.split('.'))
		print(ip.split('.', 1))

		输出:
		['aaabcde', 'fghijklmn', 'opqrst', 'uvwxyz']
		['192', '168', '0', '1']
		['192', '168.0.1']



### 元组 tuple (序列类型数据)

*  定义:
通过圆括号,中间用逗号分隔元素定义,元组和字符串一样是不可变的

		# ----定义空元组
		t0 = ()

		# ----定义单元素元组
		t1 = (1,)

		# ----元组的值无法改变,以下代码将报错!!!
		t[1] = 31 报错!

*  概念:
发展出元组类型是有原因的,利用采用字符串储存userinfo = "milo 30 male",通过这个字符串可以存储一个人的信息,但是不太好操作,取出信息不能当做一个整体,而是通过索引来进行切片操作,因此诞生元组t = ('milo', 30, 'male')

	
### 列表 list (序列类型数据)

* 定义:通过中括号,中间用逗号分隔元素定义,列表中的值是可变的

		# ----定义一个空列表
		list2 = []

		# ----定义一个元素的列表
		list3 = [1]

* 添加元素:
	
		list = [1, 2, 3]
		list.append(4)
		print(list)	
	
		输出:
		[1, 2, 3, 4]

* 删除元素:
	
		# 按照元素删除,删除第一个出现的元素,其他元素不会删除
		list3 = [1, 2, 3, 4, 1]
		list3.remove(1)
		print(list3)	
	
		输出:
		[2, 3, 4, 1]
	
		# 按照索引删除
		list3 = [1, 2, 3, 4, 1]
		del (list3[0])
		print(list3)
		
		输出:
		[2, 3, 4, 1]

* 修改元素:

		list3 = [1, 2, 3, 4, 1]
		list3[0] = 123456
		print(list3)
	
		输出:
		[123456, 2, 3, 4, 1]

### 字典 dict
*  定义:通过花括号,中间用逗号分隔元素定义.字典是Python中唯一的映射类型,无序性.

		# 通过{}创建
		dic = {0: 0, 1: 1, 2: 2}

		# 通过工厂方法dict()生成字典
		fdict = dict(['x', 1], ['y', 2])

		# fromkeys(),字典中的元素具有相同的值,默认为None,主要用于值一致的情况下
		ddict = {}.fromkeys(('x', 'y'), -1)
		ddict2 = {}.fromkeys(('x', 'y'))
		print(ddict)
		print(ddict2)

		输出:
		{'y': -1, 'x': -1}
		{'y': None, 'x': None}

*  循环遍历字典 (注意无序性!)

		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}

		# 遍历key
		for key in dic5:
	    	print(key)

		# 遍历value
		for key in dic5:
	    	print(dic1[key])

		输出:
		gender
		age
		name
		male
		13
		hebw
		
		# 同时遍历key和value
		dict2 = {'a': 1, 'b': 2, 'c': 3}
		big = dict2.items()
		for k, v in big:
		    print(k)
		    print(v)
		
		输出:
		a
		1
		c
		3
		b
		2

*  添加键值对
 
		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
		dic5['tel'] = '13100000000'
		print(dic5)

		输出:
		{'gender': 'male', 'age': 13, 'tel': '13100000000', 'name': 'hebw'}

* 删除键值对

		# del()删除key对应的键值对
		dic5 = {'gender': 'male', 'age': 13, 'tel': '13100000000', 'name': 'hebw'}
		del (dic5['tel'])

		# pop()删除key对应的键值对,并且返回该值
		dic5 = {'gender': 'male', 'age': 13, 'tel': '13100000000', 'name': 'hebw'}
		tel = dic5.pop("tel")
		print(dic5)
		print(tel)
		
* 修改值

		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
		dic5['name'] = 'HEBW'
		print(dic5)
		输出:
		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}

* 清空字典

		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
		dic5.clear()

* 判空

		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
		print("HEBW" in dic5)
		print("age" in dic5)

		输出:
		False
		True

* 删除整个字典

		dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
		del (dic5)
		print(dic5)

		输出:
		会报错,提示dic5未定义

* 根据key获取value

		# 如果存在则返回,不存在返回指定的值或none
		dic = {0: 0, 1: 1, 2: 2}	
		print(dic.get(13))
		print(dic.get(1, "error"))
		
		输出:
		None
		1

* 获取字典中键(key)的列表

		dic = {0: 0, 1: 1, 2: 2}			
		print(dic.keys())

		输出:
		[0, 1, 2]

* 获取字典中值(value)的列表

		dic = {0: 0, 1: 1, 2: 2}	
		print(dic.values())

		输出:
		[0, 1, 2]

* 获取键值对元组的列表

		dic = {0: 0, 1: 1, 2: 2}
		print(dic.items())

		输出:
		[(0, 0), (1, 1), (2, 2)]

## 序列类型基本操作

###	索引:

	序列类型容器里的元素存在索引,第一个是从0开始往后递增,
	索引分正负,如下:
	s = abcde
	 a b c d e
	 0 1 2 3 4
	-5-4-3-2-1
	
	print(s[0] + s[1])
	print(s[-1] + s[-2])
	输出:
	ab
	ed

###	切片:
	顾名思义,截取序列数据中的一部分内容

	
	# ----切片 [开始:结束:间隔默认为1,有调整切片方向的作用] 默认从左向右切片
	# ----切片 正索引
	print(s[0:1])
	print(s[:4])
	print(s[2:])
	print(s[2::2])
	
	输出:
	a
	abcd
	cde
	ce

	# ----切片 负索引
	print(s[-1])
	print(s[-1:])
	print(s[-1::-1])
	print(s[-4:-1])
	print(s[-1:-4:-1])
	print(s[-2:-5:-1])
	
	输出:
	e
	e
	edcba
	bcd
	edc
	dcb

###	长度:
	str = 'abcde'
	print(len(str))

	输出:
	5

###	连接:
	str = 'abcde'
	str2 = '12345'
	print(str + str2)

	输出:
	abcde12345
	
###	重复:
	str2 = '12345'
	print(str2 * 5)

	输出:
	1234512345123451234512345
	
### 存在判断:
	str2 = '12345'
	print('1' in str2)

	输出:
	True

### 最大值:
	str = 'abcde'
	str2 = '12345'
	print(max(str))
	print(max(str2))

	输出:
	e
	5

### 最小值:
	str = 'abcde'
	str2 = '12345'
	print(min(str))
	print(min(str2))

	输出:
	a
	1

### 比较: 这个有点不懂?
	str = 'abcde'
	str2 = '12345'	
	print(cmp(str, str2))
	print(cmp(str, str))

	输出:
	1
	0

### 遍历

	list = [1, 2, 3, 4, 5, 6, 7]
	str = 'hello'

	# 取出序列的值
	for x in list:
    	print(x)
	for x in str:
    	print(x)
	
	输出:
	1
	2
	3
	4
	5
	6
	7
	h
	e
	l
	l
	o

	# 取出序列的索引
	list = [1, 2, 3, 4, 5, 6, 7]
	for x in range(len(list)):
	    print(x)
	
	输出:
	0
	1
	2
	3
	4
	5
	6

### 筛选 filter(x,y) 第一个参数是函数,返回值是逻辑值 True 或 False
	
	l = (1, 2, 3, 4, 5, 6, 7, 8)
	def f(x):
	    if x > 5:
	        return True
	print(filter(lambda x: x == 5, l))
		
	输出:
	(5,)

### 压缩,糅合 最后返回一个元素是元组的列表 区分zip和map 还有短板的时候各自的表现
		
	# 存在三个列表
	name = ['mili', 'zou', 'yang']
	age = [23, 12, 44]
	male = ["male", 'female', 'male']
	
	# 调用zip()函数
	print(zip(name, age, male))
	# 调用map()函数
	print(map(None, name, age, male, test))

	输出:
	[('mili', 23, 'male'), ('zou', 12, 'female'), ('yang', 44, 'male')]
	[('mili', 23, 'male'), ('zou', 12, 'female'), ('yang', 44, 'male')]

	# zip()和map()在糅合的列表长度不足时的表现
	test = [1, 2]
	print(zip(name, age, male, test))
	print(map(None, name, age, male, test))
	
	输出:
	[('mili', 23, 'male', 1), ('zou', 12, 'female', 2)]
	[('mili', 23, 'male', 1), ('zou', 12, 'female', 2), ('yang', 44, 'male', None)]

	# 当map()第一个参数为函数时的表现
	a = [1, 2, 3]
	b = [4, 5, 6]
	print(map(lambda x, y: x * y, a, b))
	
	输出:
	[4, 10, 18]

### reduce() 将序列的前两个数做第一个参数定义的函数的动作,然后将数再交给第三个数,一直这样进行下去
	
	# 计算1-100相加的值
	a = reduce(lambda x, y: x + y, xrange(1, 101))
	print(a)

	输出:
	5050

	
## 流程控制语句

### 基本使用 
	
	# 两种结果
	a = 15
	if a > 124:
	    print('a > 124')
	    print('True')
	else:
	    print('a < 124')
	    print('False')

	输出:
	a < 124
	False

	# 三种结果
	a = 15
	if a > 124:
	    print('a > 124')
	    print('ok')
	elif a == 124:
	    print("a == 124")
	else:
	    print('a < 124')
	    print('false')

### 逻辑值

	True 表示非空的量
	False 表示0 NONE 空的量等

## 循环控制语句
	
### else
	# 循环正常结束后调用 
	s = 'hello'
	for k in s:
	    print(k)
	else:
	    print("ending")

	输出:
	h
	e
	l
	l
	o
	ending

### break
	
	# 打断此层的循环
	for k in s:
	    print(k)
	    if k == 'l':
	        break;
	else:
		print("ending")

	输出:
	h
	e
	l

### continue 
	
	# 跳过循环的后续代码块
	for k in s:
	    if k == 'l':
	        continue;
	    print(k)
	else:
	    print("ending")

	输出:
	h
	e
	o
	ending

### return

	# 跳出循环结束函数返回数值
	def ret():
	    for x in 'hello':
	        print(x)
	        if x == 'e':
	            return 1
	        print('666')
	    else:
	        print('-----ending')
	
	
	a = ret()
	print(a)

	输出:
	e
	1

## while循环

	# 基本使用
	x = ''
	while x != 'q':
	    print(True)
	    x = input('请输入q结束循环:')
	    if not x:
	        break;
	    if x == 'c':
	        print('one more time~~c')
	else:
	    print('ending')

## 函数

### 设置默认参数

	def fa(name="hebw", age=0):
    	print('name:%s' % name + '  age:%s' % age)
	fa()

	输出:
	name:hebw  age:0

### 直接向函数传入元组

	# 类似这样的函数,形式参数类似一个元组
	def f(x, y):
    	print x, y	
	# 这里有一个元组,如何把元组直接传入方法内.分别当做x,y
	t = (1, 2)
	# 这里使用这个方法来直接传入一个元组 利用一个*号
	f(*t)

### 直接向函数传入字典

	def fa(name="hebw", age=0):
    	print('name:%s' % name + '  age:%s' % age)
	fa(**{'age': 123, 'name': 'hbwwww'})

	输出:
	name:hbwwww  age:123

### 冗余参数的接收

	# 使用元组接收冗余参数

	def f2(x, *args):
	    print(x)
	    print(args)
	f2(2, 1)

	输出:
	2
	(1,)

	# 使用字典接收冗余参数

	def f3(x, **args):
	    print(x)
	    print(args)
	f3(1)
	f3(1, y=1)

	输出:
	1
	{}
	1
	{'y': 1}

## lambda匿名函数

	# 普通函数
	def lam(x, y):
    	return x + y
	a = lam(x=1, y=2)
	b = lam(*(3, 7))
	print(a)
	print(b)

	输出:
	3
	10

	# lambda函数
	def l(x, y):
    	return x * y
	g = lambda x, y: x * y
	
	print(type(g))
	print(id(g))
	print(g)
	print(g(2, 2))

	输出:
	<type 'function'>
	39222184
	<function <lambda> at 0x0000000002567BA8>
	4

	# lambda用法举例
	l = range(1, 6)
	def fa(x, y):
    	return x * y
	a = reduce(fa, l)
	c = reduce(lambda x, y: x * y, l)
	print(a)
	print(c)

	输出:
	120
	120

## switch场景,python不存在switch关键字,可以使用字典替代
	
	# 举例 设计一个计算器
	
	# 计算器
	def add(x, y):
	    return x + y
	
	
	def jian(x, y):
	    return x - y
	
	
	def cheng(x, y):
	    return x * y
	
	
	def chu(x, y):
	    return x / y

	# 用if 和 else 写的代码
	def operator(x, o, y):
	    if o == "+":
	        return add(x, y)
	    elif o == '-':
	        return jian(x, y)
	    elif o == '*':
	        return cheng(x, y)
	    elif o == '/':
	        return chu(x, y)
	    else:
	        pass

	
	print(operator(6, '+', 6))
	
	输出:
	12

	# 用字典的方法
	oper = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y,
        '/': lambda x, y: x / y}

	def fc(x, o, y):
    	print(oper.get(o)(x, y))

	fc(12, '/', 2)

	输出:
	6

	# 总结:
	# {}.get('o')('1', '2')
	# 前面的{}代表字典,利用get方法,获取字典对应的value,value可以是一个lambda方法,同时可以直接在后传入方法的参数

## 内置函数
	
### abs() 返回数字的绝对值

	a = abs(-10111111)
	print(a)
	print(type(a))
	
	输出:
	10111111
	<type 'int'>

### max()最大 min()最小

	l = [1, 23, 4, 5, 6, 7, 8, 9, 0, 1, 3, 23, 2, 2, 31, 5, 7, 89, 34, 23, 'sd']
	print(max(l))
	print(min(l))

	输出:
	sd
	0

### divmod() 返回包含两个数字的商和余的元组
	
	print(divmod(2, 5))

	输出:
	(0,2)

### pow(x, y[, z]) 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
	
	print(pow(2, 3, 4))

	输出:
	0

### round() 四舍五入
	
	print(round(12.4))

	输出:
	12.0
	
### callable() 检测函数是否可以被调用

	print(callable(round))
	
	输出:
	True

### isinstance() 判断对象是否属于某类型

	l2 = {1: 1, 2: 2}
	print(isinstance(l2, tuple))

	输出:
	False

### cmp() 判断两个字符串是否一样
	
	print(cmp('1', '1'))
	print(cmp('1', '2'))
	print(cmp('2', '1'))

	输出:
	0
	-1
	1

### xrange()相比range(),就说是效率高一点,具体用处不明啊


### 类型转换

	print(type(int(123)))
	print(type(long(123)))
	print(type(float(123)))
	print(type(tuple([1, 2])))
	print(type(list((1,))))
	print(type(str(1)))

	输出:
	<type 'int'>
	<type 'long'>
	<type 'float'>
	<type 'tuple'>
	<type 'list'>
	<type 'str'>

## 正则表达式

* 定义:re模块
	
		# 定义一个普通正则
		s1 = 'abc'
		s1Req = r'abc'
		a = re.findall(s1Req,s1)
		print(a)
		print(type(a))
		
		输出:
		['abc']
		<type 'list'>

* 字符集 []
	
		# 普通正则里存在一个字符集,表示字符集里的情况都可以
		s1 = 'abc'
		s3 = r'a[bcd]c'
		a = re.findall(s3,s1)
		print(a)

		输出:
		['abc']

* 匹配行首和非的情况 ^ 

		# ^放在字符集的开头,表示非bcd的情况都可以
		s1 = 'abc'
		s4 = r'a[^bcd]c'
		print(re.findall(s4,s1))

		输出:
		[]

		# ^放在字符集的非开头位置,就是一个普通符号
		s1 = 'abc'
		s4 = r'a[bcd^]c'
		print(re.findall(s4,s1))

		输出:
		['abc']

		# ^不存在于字符集中,仅仅放在匹配开头
		s1 = 'abc'
		s6 = r'^abc'
		print(re.findall(s6, s1))

		输出:
		['abc']

* 匹配行尾 $

		# 匹配行尾
		s1 = 'abc'
		s7 = r'abc$'
		print(re.findall(s7, s1))

		输出:
		['abc']

* 匹配范围字符
		
		# 数字0-9
		s8 = r'[0-9]'
		s8 = r'\d'

		# 非数字0-9
		s8 = r'[^0-9]'
		s8 = r'\D'

		# 匹配空白字符
		ss = r'\s'
		# 匹配非空白字符
		ss = r'\S'
		
		# 匹配任何字母数字字符(包括下划线)
		sw = r'[a-zA-Z0-9_]'
		sw = r'\w'
		
		# 匹配任何非字母数字字符
		sw = r'\W'

* 注意转义
		
		# 如果想要取^abc,在规则当中将^转换为普通符号,用反斜杠转义
		s1 = '^abc'
		s10 = r'\^abc'
		print(re.findall(s10, s1))
		
		输出:
		['^abc']

* 匹配不定长的字符集,指定一部分字符集重复的次数
		
		mobile = '010-12345678'

		# 举例:匹配电话号码,数字可以出现8次
		sm = r'^010-\d{8}'
		
		# 举例:最少重复3次,最多重复8次
		sm = r'^010\d{3,8}'

		# 举例:{0,}等同于*,{1,}等同于+,{0,1}等同于?
		
		# 举例:匹配b可以出现0-N次
		st = r'a[b]*'
		str = 'abbbbbbbaab'
		print(re.findall(st, str))
		
		输出:
		['abbbbbbb', 'a', 'ab']
		
		# 举例:匹配b可以出现1-N次
		st = r'a[b]+'
		str = 'abbbbbbbaab'
		print(re.findall(st, str))
		
		输出:
		['abbbbbbb', 'ab']

		# 举例:匹配一次或零次
		str = 'abbbbbbbaab'
		st2 = r'ab?'
		print(re.findall(st2, str))

		输出:
		['ab', 'a', 'ab']
		
		# 举例:非贪婪匹配,让重复次数变为最小匹配数为1
		str = 'abbbbbbbaaba'
		st1 = r'ab+?'
		print(re.findall(st1, str))
		
		输出:
		['ab', 'ab']

* 编译后的正则效率更高
		
		# 未编译的正则
		r1 = r'\d{3,4}-?\d{8}$'
		print(re.findall(r1, "010-12345678"))

		# 编译的正则 效率更高, 编译后的类型变为 _sre.SRE_Pattern
		p_tel = re.compile(r1)
		print(p_tel)
		print(p_tel.findall('010-12345678'))

		输出:
		<_sre.SRE_Pattern object at 0x00000000024C9688>
		['010-12345678']
		
		# 不区分大小写 取决于编译时的模式
		csvt_re = re.compile(r'csvt', re.I)
		print(csvt_re.findall('CsVt'))

		输出:
		['CsVt']
		
		# match()方法 只有被匹配数据在开头才会返回一个对象,否则为None
		csvt_re = re.compile(r'csvt', re.I)
		print(csvt_re.match('hello csvt'))

		输出:
		None

		# search() 不管匹配元素在什么位置都可以找到,没有则为None
		
		print(csvt_re.search('hello csvt'))
		print(csvt_re.search('hello csvt').group())
		print(csvt_re.search('hello csvt').start())
		print(csvt_re.search('hello csvt').end())
		print(csvt_re.search('hello csvt').span())

		输出:
		<_sre.SRE_Match object at 0x0000000002402578>
		csvt
		6
		10
		(6, 10)

		# finditer() 返回一个迭代器的对象,不太懂
		x = csvt_re.finditer('hello csvt')
		print(x)

		# re.S 使.匹配包括换行在内的所有字符
		r1 = r'csvt.net'
		a = re.findall(r1, 'csvt\nnet', re.S)
		a2 = re.findall(r1, 'csvtOnet', re.S)
		print(a)
		print(a2)

		输出:
		['csvt\nnet']
		['csvtOnet']

		# re.X 字符串多行的情况下,匹配行首
		s = """ 
		hello csvt
		csvt hello
		hello csvt hello
		csvt hehe
		"""
		r = r'^csvt'
		print(re.findall(r, s))
		print(re.findall(r, s, re.M))
			
		输出:
		[]
		['csvt', 'csvt']

* 举例:匹配邮箱地址.关键是结尾的元素有几个可能

		# 使用后面的括号包裹,分组.在分组中可以'或 | '等其他操作
		email = r'\w{3}@\w+(\.com|\.cn)'
		print(re.match(email, 'zzz@csvt.com'))
		print(re.match(email, 'zzz@csvt.cn'))
		print(re.match(email, 'zzz@csvt.org'))

		输出:
		<_sre.SRE_Match object at 0x00000000026F5BE8>
		<_sre.SRE_Match object at 0x00000000026F5BE8>
		None


		# 当存在分组的时候,在匹配的时候会优先返回分组中的数据
		email = r'\w{3}@\w+(\.com|\.cn)'
		print(re.findall(email, 'zzz@csvt.com'))

		输出:
		['.com']

* 举例:网页爬虫
		
		# 关键:关键两步,1.利用模块将网页代码爬下,2.利用正则解析出其中的图片并用模块下载到本地
		
		源码如下:

		import re
		import urllib

		def getHtml(url):
			# 获取网页代码
    		return urllib.urlopen(url).read()

		def getImg(html):
			# 目标图片字符串
		    # src="//www.baidu.com/img/bd_logo1.png"
		    # r1 = r'src="(.*?\.png)"'
		    r1 = r'src="//(.*?\.png)"'

			# 编译正则
		    imgRe = re.compile(r1)
			
		    print(imgRe.findall(html))
		
		    x = 0
			# 遍历获取到的图片地址列表
		    for i in imgRe.findall(html):
		        fileName = "图片%s.png" % x
		        print(fileName)
				# 下载照片到本地,路径默认为与该文件同一个目录下
		        urllib.urlretrieve('http://' + i, fileName)
		        x += 1
		    print "Download Pictures!!!"

		# html = getHtml("https://www.baidu.com/")
		html = getHtml("https://daohang.qq.com/?fr=hmpage")
		getImg(html)

## 深拷贝和浅拷贝 

* 总结:依赖于copy模块,区别在于拷贝的新对象的内存地址和对象包含的元素的内存地址是不是都是新的一个内存地址

		# b = a ,修改a会导致b也变化,因为a b都是指向同一个内存空间
		a = [1, 2, 3, ['a', 'b', 'c']]
		b = a
		a.append(1)
		print(id(a))
		print(id(b))
		print(b)
	
		输出:
		40395784
		40395784
		[1, 2, 3, ['a', 'b', 'c'], 1]
	
		# 浅拷贝 c指向另一个内存空间 增删a的元素不会导致c发生改变,但是修改a的元素会导致c发生变化
		a = [1, 2, 3, ['a', 'b', 'c']]
		c = copy.copy(a)
		a.append(6)
		print(id(a))
		print(id(c))
		print(a)
		print(c)
	
		输出:
		40264712
		40321480
		[1, 2, 3, ['a', 'b', 'c'], 1, 6]
		[1, 2, 3, ['a', 'b', 'c'], 1]
	
		# 浅拷贝,虽然不存在同一个内存空间,但是包含的元素还是在同一个内存空间,修改元素还是会同时改变
		print(id(a[3]))
		print(id(c[3]))
		a[3].append('d')
		print(c)
		
		输出:
		40265928
		40265928
		[1, 2, 3, ['a', 'b', 'c', 'd'], 1]

		# 深拷贝 理解为将所有的数据都拷贝出来
		d = copy.deepcopy(a)
		print(id(a))
		print(id(d))
		print(id(a[3]))
		print(id(d[3]))
		
		输出:
		40264712
		40276936
		40265928
		40323656

## 文件读写

* mode模式

		# r 只读
		# r+ 读写 这时候写入会从开头开始覆盖原文件的内容
		# w 写入 先删除原文件,再重新写入,如果文件没有则创建
		# w+ 读写 先删除原文件,再重新写入,如果文件没有则创建
		# a 写入: 在文件末尾追加新的内容,文件不存在则创建
		# a+ 读写: 在文件末尾追加新的内容,文件不存在则创建
				
* 文件的打开

		fo = open('test.txt', 'r+')
		print(fo)

		输出:
		<open file 'test.txt', mode 'r+' at 0x00000000025371E0>

* 文件的读取 注意关闭,关闭后无法再次读取

		fo = open('test.txt', 'r+')
		print(fo.read())
		fo.close()

		输出:
		(文件内容)

* 文件的写入,与mode有关系,决定覆盖写入还是从尾部添加

		fo = open('test.txt', 'r+')
		fo.write('aaaaaaaaaaa')
		fo.close()
		
* 循环
		f = open('test.txt', 'r')
		for i in open('test.txt'):
    		print(i)

		输出:
		aaaaaaaaaaathello

		i am hebwhell
		
		hellooneloHello
		
		twohello
		
		threehel

* 读取一行 readline() 每次读取一行 超出范围后返回None
		
		f = open('test.txt', 'r')
		print(f.readline())

* readlines() 返回一个包含各行元素的列表

		f = open('test.txt', 'r')
		print(f.readlines())
		
		输出:
		['aaaaaaaaaaathello\n', 'i am hebwhell\n', 'hellooneloHello\n', 'twohello\n', 'threehel\n']

* next() 每次读取一行 超出则报错StopIteration

		f = open('test.txt', 'r')
		print(f.next())

* writelines()实现多行写入,效率比write更高,少量写入则建议用write
		
		f = open('test.txt', 'r')
		l = ['one\n', 'two\n', 'three\n']
		f.writelines(l)

* seek(x,y)移动指针

		# read读取并且文件的指针会跳到最后 
		# seek可以将指针设置到指定的位置
		#  x 表示偏移量,可以为负数.正向右偏移,负向左偏移
		#  y 表示选项
		#       0 表示将指针从文件开头到偏移量字节处
		#       1 表示将指针从文件当前位置到偏移量字节处
		#       2 表示将指针从文件末尾到偏移量字节处

		f = open('test.txt', 'r')
		print('第一次读取' + f.read())
		f.seek(-3, 2)
		print('第二次读取' + f.read())

		输出:
		第一次读取aaaaaaaaaaathello
		i am hebwhell
		hellooneloHello
		twohello
		threehel
		
		第二次读取l

* flush 提交更新,将缓存区内的数据及时提交到文件当中
		
* 举例:统计文件中Hello的个数
		
		'test.txt'文件内容:
		aaaaaaaaaaathello
		i am hebwhell
		hellooneloHello
		twohello
		threehel


		f = open('test.txt', 'r')
		content = f.read()
		f.close()
		hiReg = r'hello'
		# 正则匹配,忽略大小写
		helloReg = re.compile(hiReg, re.I)
		hiList = helloReg.findall(content)
		print(len(hiList))

* 举例:替换文件中的hello并另存为其他文件(还可以拓展为替换hello的同时忽略大小写)
		
		'test.txt'文件内容:
		aaaaaaaaaaathello
		i am hebwhell
		hellooneloHello
		twohello
		threehel

		# 区分大小写
		f = open('test.txt', 'r')
		content = f.read()
		f2 = file('new.txt','w')
		f2.write(content.replace('hello','csvt'))
		f2.close()
		f.close()
		
		# 不区分大小写
		f = open('test.txt', 'r')
		content = f.read()
		f2 = file('new.txt','w')
		content2 = re.sub(r'(?i)hello', 'csvt', content)
		f2.write(content2)
		f2.close()
		f.close()

## 文件操作OS模块
		
		# 创建一个目录(文件夹)
		os.mkdir("test")

		# 创建一个目录(文件夹),可以嵌套
		os.makedirs("a/b/c")

		# 删除一个(文件夹),例如:a/b/c,只删除c
		os.rmdir("a/b/c")

		# 删除一个(文件夹),可以嵌套删除,例如:a/b/c,全部删除
		os.removedirs("a/b/c")

		# 返回一个列表,包含文件夹中的所有文件和目录,不包含子目录
		list = os.listdir("C:/Users/A13201/Desktop/pythonStudy")

		# 返回根目录的列表 比如 c盘
		list = os.listdir("/")

		# 返回当前目录文件文件夹列表
		list = os.listdir(".") 
		
		# 获取当前路径
		cwd = os.getcwd()

		# 切换目录
		os.chdir("/")

		# 切换到根目录
		os.chdir("C:/Users/A13201/Desktop")

		# 举例:遍历一个目录,返回包括子目录的文件绝对路径
		