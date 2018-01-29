#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-22 21:43:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


def test1():
    count = input('请输入你的幸运数：')
    # length = len(count)

    # for i in range(1, int(count) + 1):
    #     formatStr = '{:0>' + str(length) + '}'
    #     print("I Love Python ... %s" % (formatStr.format(str(i))))
    i = 0
    while i <= int(count):
        print('I Love Tmy', str(i).zfill(3))
        i += 1


def test2():
    srcStr = input('请输入一段文字：')
    destStr = input('请输入目标字符串：')

    print(distStr, '在', srcStr, '中出现的次数为：', srcStr.count(destStr))


def test3():
    inStr = input('请输入一个整数：')

    while inStr != 'EOF':
        result = 0
        for i in range(1, int(inStr) + 1):
            result += i
        print(result)
        inStr = input('请输入一个整数：')


if __name__ == '__main__':
    test1()
