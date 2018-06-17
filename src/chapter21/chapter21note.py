# coding:utf-8
# usr/bin/python3
# python src/chapter21/chapter21note.py
# python3 src/chapter21/chapter21note.py
'''

Class Chapter21_1

Class Chapter21_2

Class Chapter21_3

Class Chapter21_4

'''
from __future__ import absolute_import, division, print_function

import math as _math
import random as _random
import time as _time
from copy import copy as _copy
from copy import deepcopy as _deepcopy
from random import randint as _randint

import numpy as np
from numpy import arange as _arange
from numpy import array as _array
from numpy import * 

if __name__ == '__main__':
    import notintersectset as _nset
else:
    from . import notintersectset as _nset

class Chapter21_1:
    '''
    chpater21.1 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter21.1 note

        Example
        ====
        ```python
        Chapter21_1().note()
        ```
        '''
        print('chapter21.1 note as follow')  
        print('第21章 用于不相交集合的数据结构')
        print('某些应用中，要将n个不同的元素分成一组不想交的集合')
        print('不相交集合上有两个重要的操作，即找出给定的元素所属的集合和合并两个集合')
        print('为了使某种数据结构能够支持这两种操作，就需要对该数据结构进行维护；本章讨论各种维护方法')
        print('21.1描述不相交集合数据结构所支持的各种操作，并给出这种数据结构的一个简单应用')
        print('21.2介绍不想交集合的一种简单链表实现')
        print('21.3采用有根树的表示方法的运行时间在实践上来说是线性的，但从理论上来说是超线性的')
        print('21.4定义并讨论一种增长极快的函数以及增长极为缓慢的逆函数')
        print(' 在基于树的实现中，各操作的运行时间中都出现了该反函数。',
            '然后，再利用平摊分析方法，证明运行时间的一个上界是超线性的')
        print('21.1 不相交集合上的操作')
        print('不相交集合数据结构保持一组不相交的动态集合S={S1,S2,...,Sk}')
        print('每个集合通过一个代表来识别，代表即集合中的某个成员')
        print('集合中的每一个元素是由一个对象表示的，设x表示一个对象，希望支持以下操作')
        print('MAKE-SET(x)：其唯一成员(因而其代表)就是x。因为各集合是不相交的，故要求x没有在其他集合出现过')
        print('UNION(x, y)：将包含x和y的动态集合(比如说Sx和Sy)合并为一个新的集合(并集)')
        print('FIND-SET(x)：返回一个指针，指向包含x的(唯一)集合的代表')
        print('不相交集合数据结构的一个应用')
        # !不相交集合数据结构有多种应用,其中之一是用于确定一个无向图中连通子图的个数
        print(' 不相交集合数据结构有多种应用,其中之一是用于确定一个无向图中连通子图的个数')
        g = _nset.UndirectedGraph()
        g.vertexs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
        g.edges = [('d', 'i'), ('f', 'k'), ('g', 'i'),
                   ('b', 'g'), ('a', 'h'), ('i', 'j'), 
                   ('d', 'k'), ('b', 'j'), ('d', 'f'), 
                   ('g', 'j'), ('a', 'e'), ('i', 'd')]
        print('练习21.1-1') 
        print(' 无向图G=(V, E)的顶点集合V=')
        print('  {}'.format(g.vertexs))
        print(' 边集合E=')
        print('  {}'.format(g.edges))
        print(' 所有连通子图的顶点集合为')
        print('  {}'.format(g.get_connected_components()))
        print('练习21.1-2 证明：在CONNECTED-COMPONENTS处理了所有的边后')
        print(' 两个顶点在同一个连通子图中，当且仅当它们在同一个集合中')
        print('练习21.1-3 无向图G=(V,E)调用FIND_SET的次数为len(E)*2,',
            '调用UNION的次数为len(V) - k')
        g.print_last_connected_count()
        # python src/chapter21/chapter21note.py
        # python3 src/chapter21/chapter21note.py

class Chapter21_2:
    '''
    chpater21.2 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter21.2 note

        Example
        ====
        ```python
        Chapter21_2().note()
        ```
        '''
        print('chapter21.2 note as follow')
        print('21.2 不相交集合的链表表示')
        print(' 要实现不相交集合数据结构，一种简单的方法是每一种集合都用一个链表来表示')
        print(' 每个链表中的第一个对象作为它所在集合的代表')
        print(' 链表中的每一个对象都包含一个集合成员，一个指向包含下一个集合成员的对象的指针，以及指向代表的指针')
        print(' 每个链表都含head指针和tail指针，head指向链表的代表，tail指向链表中最后的对象')
        print(' 在这种链表表示中，MAKE-SET操作和FIND-SET操作都比较容易实现，只需要O(1)的时间')
        print(' 执行MAKE-SET(x)操作，创建一个新的链表,其仅有对象为x')
        print(' 对FIND-SET(X)操作,只要返回由x指向代表的指针即可')
        print('合并的一个简单实现')
        print(' 在UNION操作的实现中，最简单的是采用链表集合表示的实现，',
            '这种实现要比MAKE-SET或FIND-SET多不少的时间')
        print(' 执行UNION(x,y),就是将x所在的链表拼接到y所在链表的表尾.利用y所在链表的tail指针',
            '可以迅速地找到应该在何处拼接x所在的链表')
        print(' 一个作用于n个对象上的,包含m个操作的序列，需要Θ(n^2)时间')
        print(' 执行n个MAKE-SET操作所需要的时间为Θ(n)')
        print(' 因为第i个UNION操作更新了i个对象，故n-1个UNION操作所更新的对象总数为Θ(n^2)')
        print(' 总的操作数为2n-1，平均来看，每个操作需要Θ(n)的时间')
        print(' 也就是一个操作的平摊时间为Θ(n)')
        print('一种加权合并启发式策略')
        print(' 在最坏情况下，根据上面给出的UNION过程的实现，每次调用这一过程都需要Θ(n)的时间')
        print(' 如果两个表一样长的话，可以以任意顺序拼接，利用这种简单的加权合并启发式策略')
        print(' 如果两个集合都有Ω(n)个成员的话，一次UNION操作仍然会需要Θ(n)时间')
        print('定理21.1 利用不相交集合的链表表示和加权合并启发式',
            '一个包括m个MAKE-SET,UNION和FIND-SET操作',
            '(其中有n个MAKE-SET操作)的序列所需时间为O(m+nlgn)')
        print('练习21.2-1 已经完成')
        print('练习21.2-2 如下:结果是16个链表集合合并成了一个总的链表')
        _nset.test_list_set()
        print('练习21.2-3 对定理21.1的证明加以改造，使得MAKE-SET和FIND-SET操作有平坦时间界O(1)')
        print(' 对于采用了链表表示和加权合并启发式策略的UNION操作，有界O(lgn)')
        print('练习21.2-4 假定采用的是链表表示和加权合并启发式策略。略')
        print('练习21.2-5 合并的两个表像合并排序那样轮流交叉合并')
        # python src/chapter21/chapter21note.py
        # python3 src/chapter21/chapter21note.py

class Chapter21_3:
    '''
    chpater21.3 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter21.3 note

        Example
        ====
        ```python
        Chapter21_3().note()
        ```
        '''
        print('chapter21.3 note as follow')
        print('21.3 不相交集合森林')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        # python src/chapter21/chapter21note.py
        # python3 src/chapter21/chapter21note.py

class Chapter21_4:
    '''
    chpater21.4 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter21.4 note

        Example
        ====
        ```python
        Chapter21_4().note()
        ```
        '''
        print('chapter21.4 note as follow')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        # python src/chapter21/chapter21note.py
        # python3 src/chapter21/chapter21note.py

chapter21_1 = Chapter21_1()
chapter21_2 = Chapter21_2()
chapter21_3 = Chapter21_3()
chapter21_4 = Chapter21_4()

def printchapter21note():
    '''
    print chapter21 note.
    '''
    print('Run main : single chapter twenty-one!')  
    chapter21_1.note()
    chapter21_2.note()
    chapter21_3.note()
    chapter21_4.note()

# python src/chapter21/chapter21note.py
# python3 src/chapter21/chapter21note.py
if __name__ == '__main__':  
    printchapter21note()
else:
    pass
