#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-16 22:09:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# Python允许你同时为多个变量赋值

a = b = c = 1
d, e = 1, 'hello world'

'''
标准数据类型
Python3 中有六个标准的数据类型：
    - Number（数字）
    - String（字符串）
    - List（列表）
    - Tuple（元组）
    - Sets（集合）
    - Dictionary（字典）

查看变量类型 type(var), e.g. type(123) ==> <class 'int'>
判断变量类型 isinstance(var, type), e.g. isinstance(123, int) ==> True
两者的区别：
    - type() 不会认为子类是一种父类类型
    - isinstance() 会认为子类是一种父类类型
'''

# Number
'''
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
'''

# 数值运算
'''
    >>>5 + 4  # 加法
    9
    >>> 4.3 - 2 # 减法
    2.3
    >>> 3 * 7  # 乘法
    21
    >>> 2 / 4  # 除法，得到一个浮点数
    0.5
    >>> 2 // 4 # 除法，得到一个整数
    0
    >>> 17 % 3 # 取余 
    2
    >>> 2 ** 5 # 乘方
    32

- 数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
- 在混合计算时，Python 会把整型转换成为浮点数。
'''

# String
'''
Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串不能被改变

索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。
'''

'''
str = 'Runoob'
 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str[:])       # 输出复制字符串
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串
'''
