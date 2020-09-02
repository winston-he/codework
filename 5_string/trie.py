#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: trie.py
@Time: 2020/8/30 20:14
'''
"""
字典树（前缀树）
实现字典树的4个功能：
    - 添加单词 insert
    - 删除单词 delete
    - 查询单词是否在字典树中 search
    - 返回以字符串pre为前缀的单词数量 prefixCount
"""


class TrieNode:
    def __init__(self):
        self.path = 0  # 有多少个单词共用这个节点
        self.end = 0  # 有多少个单词以这个节点结尾
        self.map = dict() # 这个节点的路径

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        if not word:
            return
        self.root.path += 1
        curr = self.root
        for w in word:
            if w not in curr.map or curr[w] is None:
                curr.map[w] = TrieNode()
            curr = curr.map[w]
            curr.path += 1
        curr.end += 1

    def delete(self, word: str):
        if not self.search(word):
            return
        self.root.path += 1
        curr = self.root
        for w in word:
            curr.map[w].path -= 1
            if curr.map[w].path == 0:
                curr.map[w] = None
                return
            curr = curr.map[w]


    def search(self, word: str):
        pass

    def prefix_count(self, pre: str):
        pass

