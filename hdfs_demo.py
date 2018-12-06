#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 18:56
# @Author  : Trojx
# @File    : hdfs_demo.py

from hdfs import InsecureClient

if __name__ == '__main__':
    root_path = "/"
    client = InsecureClient(url="http://localhost:50070", user='root', root=root_path)
    client.makedirs('/dir_by_python')
    print(client.list('/'))
    client.upload('/dir_by_python','Dockerfile')
    print(client.list('/'))