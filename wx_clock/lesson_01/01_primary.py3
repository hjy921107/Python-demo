#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 1. 获取关注列表的真实路径，注：{} 见 url.format()
url = 'https://zhuanlan.zhihu.com/api/columns/wajuejiprince/followers?limit={}'
# 2. 设置请求头，模拟请求
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'
}
# 3. 获取 response
resp = requests.get(url.format(1000), headers=headers)
# 4. 数据 json 处理
followers_list_json = resp.json()
# 5. 遍历 json 列表，获取关注者相关信息
for follower in followers_list_json:
    uid = follower['uid']
    bio = follower['bio']
    name = follower['name']
    profileUrl = follower['profileUrl']
    print('uid: %s, bio: %s, name: %s, profileUrl: %s' %
          (uid, bio, name, profileUrl))
