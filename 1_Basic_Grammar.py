#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-15
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

# 字面意义级联字符串
'''
str = "this " "is " "sring"
print(str)
'''

# 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
'''
str = "this " + \
      "is " + \
      "string"
print(str)
'''
# 允许在同一行中使用多条语句，语句之间使用分号(;)分割，但并不建议
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# import 与 from...import
'''
import sys
print('=' * 20)
print('命令行参数为：', end='')
for i in sys.argv:
    print(i)
print('\n python 路径为：', sys.path)

from sys import path  # 导入特定的成员
print('=' * 10, 'print from import', '=' * 10)
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
'''
