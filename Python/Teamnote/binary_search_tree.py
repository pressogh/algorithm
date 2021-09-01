# 10870
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
    #     self.root = self._insert_value(self.root, data)
    #     return self.root is not None
        new_node = Node(data)
        cur_node = self.root
        if cur_node == None:
            self.root = new_node
            return
        while True:
            parent = cur_node
            if data < cur_node:
                cur_node = cur_node.left
                if cur_node is None:
                    parent.left = new_node
                    return
                else:
                    cur_node = cur_node.right
                    if cur_node is None:
                        parent.right = new_node
                        return
    def search(self, target):
        cur_node = self.root
        while cur_node:
            if target == cur_node.data:
                return cur_node
            if target < cur_node.data:
                cur_node = cur_node.left
            else:
                target = cur_node.right
        return cur_node
    def delete(self, target):
        self.root, deleted_node = self.__delete_recursion(self.root, target)
        deleted_node.left = None
        deleted_node.right = None
        return deleted_node
    def __delete_recursion(self, cur_node, target):
        # 대상 데이터가 트리 안에 없을 시 None 반환
        if cur_node is None:
            return None, None
        # 대상 데이터가 현재 노드의 데이터보다 크면
        if target < cur_node.data:
            # 노드의 왼쪽 자식에서 대상 데이터를 가진 노드를 지운다
            cur_node, deleted_node = self.__delete_recursion(cur_node.left, target)
        elif target > cur_node.data:
            cur_node, deleted_node = self.__delete_recursion(cur_node.right, target)
        # 대상 데이터가 현재 노드의 데이터와 같다면
        else:
            # leaf 노드 일 때
            if not cur_node.left and not cur_node.right:
                deleted_node = cur_node
                cur_node = None
            # 자식 노드가 하나일 때
            elif not cur_node.right:
                deleted_node = cur_node
                cur_node = cur_node.left
            else:
                

    # def _insert_value(self, node, data):
    #     if node is None:                                                # node가 None일시 그 node = data
    #         node = Node(data)
    #     else:
    #         if data <= node.data:                                       # node가 None이 아니라면 데이터와 현재 노트의 데이터 비교
    #             node.left = self._insert_value(node.left, data)         # 현재 노드의 데이터가 데이터보다 클 시 재귀
    #         else:
    #             node.right = self._insert_value(node.right, data)
    #     return node

bst = BST()
bst.insert(3)