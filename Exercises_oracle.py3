#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-17 14:21:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import cx_Oracle
import time

def printLog(printMsg):
    print('INFO:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), printMsg)

printLog('数据库连接...')

# 连接数据库
'''
# 方法一
dsn = cx_Oracle.makedsn('10.10.101.194', '1521', 'nhxt')
connection = cx_Oracle.connect('ecms', 'ecms', dsn)
'''
# 方法二
connection = cx_Oracle.Connection('hx', 'hx', '194_nhxt')

# 获取游标
cursor = connection.cursor()

printLog('数据库连接成功！')

# 执行普通查询 SQL
sql = '''
    SELECT 
        CONTRACTCODE, CONTRACTNAME, TRADESUM, 
        SIGNDATE, ENDDATE, APPLYUSERID, 
        APPLYUSERNAME, SUPPLIER_CODE, SUPPLIER_NAME
    FROM ECMS.CONTRACT
'''

printLog('开始执行 SQL:' + sql)

cursor.execute(sql)

# 处理游标中的数据
'''
# 方法一：获取游标全部数据
data = cursor.fetchall()
'''

# 方法二：遍历游标
# for contractcode, contractname, tradesum, signdate, enddate, applyuserid, \
#     applyusername, supplierCode, supplierName in cursor:
#     print('Value:', id, householdNumber, sep = '@')

file = open('D:\\contract.dat', 'w')

printLog('遍历数据，输出到文件...')

result = ''
count = 0
for line in cursor:
    for item in line:
        result += str(item) + '$@$'
    file.write(result.rstrip('$@$'))

printLog('输出结束，关闭游标！')

# 关闭游标
cursor.close()
