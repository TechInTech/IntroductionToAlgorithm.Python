# coding:utf-8
# usr/bin/python3
# python src/chapter26/chapter26note.py
# python3 src/chapter26/chapter26note.py
'''

Class Chapter26_1

Class Chapter26_2

Class Chapter26_3

Class Chapter26_4

Class Chapter26_5

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

if __name__ == '__main__':
    import graph as _g
else:
    from . import graph as _g

class Chapter26_1:
    '''
    chpater26.1 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter26.1 note

        Example
        ====
        ```python
        Chapter26_1().note()
        ```
        '''
        print('chapter26.1 note as follow')  
        print('第26章 最大流')
        print('为了求从一点到另一点的最短路径，可以把公路地图模型化为有向图')
        print('可以把一个有向图理解为一个流网络,并运用它来回答有关物流方面的问题')
        print('设想某物质从产生它的源点经过一个系统,流向消耗该物质的汇点(sink)这样一种过程')
        print('源点以固定速度产生该物质,而汇点则用同样的速度消耗该物质.',
            '从直观上看,系统中任何一点的物质的流为该物质在系统中运行的速度')
        print('物质进入某顶点的速度必须等于离开该顶点的速度,流守恒性质,',
            '当物质是电流时,流守恒与基尔霍夫电流定律等价')
        print('最大流问题是关于流网络的最简单的问题')
        print('26.1 流网络')
        print('流网络的流')
        print('  流网络G=(V,E)是一个有向图,其中每条边(u,v)∈E均有一非负容量c(u,v)>=0',
            '如果(u,v)∉E,则假定c(u,v)=0。流网络中有两个特别的顶点：源点s和汇点t',
            '为了方便起见，假定每个顶点均处于从源点到汇点的某条路径上，就是说,每个顶点v∈V,存在一条路径s->v->t',
            '因此,图G为连通图,且|E|>=|V|-1')
        print('流的定义')
        print('  设G=(V,E)是一个流网络，其容量函数为c。设s为网络的源点，t为汇点。',
            'G的流是一个实值函数f:V*V->R,且满足下列三个性质：')
        print('  (1) 容量限制：对所有u,v∈V,要求f(u,v)<=c(u,v)')
        print('  (2) 反对称性：对所有u,v∈V,要求f(u,v)=-f(v,u)')
        print('  (3) 流守恒性：对所有u∈V-{s,t},要求∑f(u,v)=0')
        print('  f(u,v)称为从顶点u到顶点v的流，可以为正，为零，也可以为负。流f的值定义为|f|=∑f(s,v)',
            '即从源点出发的总流.在最大流问题中,给出一个具有源点s和汇点t的流网络G,希望找出从s到t的最大值流')
        print('容量限制只说明从一个顶点到另一个顶点的网络流不能超过设定的容量',
            '反对称性说明从顶点u到顶点v的流是其反向流求负所得.',
            '流守恒性说明从非源点或非汇点的顶点出发的总网络流为0')
        print('定义某个顶点处的总的净流量(total net flow)为离开该顶点的总的正能量,减去进入该顶点的总的正能量')
        print('流守恒性的一种解释是这样的,即进入某个非源点非汇点顶点的正网络流，必须等于离开该顶点的正网络流',
            '这个性质(即一个顶点处的总的净流量必定为0)常常被形式化地称为\"流进等于流出\"')
        print('通常，利用抵消处理，可以将两城市间的运输用一个流来表示,该流在两个顶点之间的至多一条边上是正的')
        print('给定一个实际运输的网络流f,不能重构其准确的运输路线,如果知道f(u,v)=5,',
            '如果知道f(u,v)=5,表示有5个单位从u运输到了v,或者表示从u到v运输了8个单位,v到u运输了3个单位')
        print('本章的算法将隐式地利用抵消,假设边(u,v)有流量f(u,v).在一个算法的过程中,可能对边(u,v)上的流量增加d',
            '在数学上,这一操作为f(u,v)减d；从概念上看,可以认为这d个单位是对边(u,v)上d个单位流量的抵消')
        print('具有多个源点和多个汇点的网络')
        print('  在一个最大流问题中,可以有几个源点和几个汇点,而非仅有一个源点和一个汇点',
            '比如物流公司实际可能拥有m个工厂{s1,s2,...,sm}和n个仓库{t1,t2,...,tn}',
            '这个问题不比普通的最大流问题更难')
        print('  在具有多个源点和多个汇点的网络中,确定最大流的问题可以归约为一个普通的最大流问题',
            '通过增加一个超级源点s,并且对每个i=1,2,...,m加入有向边(s,si),其容量c(s,si)=∞',
            '同时创建一个超级汇点t,并且对每个j=1,2,...,n加入有向边(tj,t),其容量c(tj,t)=∞')
        print('  单源点s对多个源点si提供了其所需要的任意大的流.同样,单汇点t对多个汇点tj消耗其所需要的任意大的流')
        print('对流的处理')
        print('  下面来看一些函数(如f),它们以流网络中的两个顶点作为自变量',
            '在本章,将使用一种隐含求和记号,其中任何一个自变量或两个自变量可以是顶点的集合',
            '它们所表示的值是对自变量所代表元素的所有可能的情形求和')
        print('  流守恒限制可以表述为对所有u∈V-{s,t},有f(u,V)=0,',
            '同时,为方便起见,在运用隐含求和记法时,省略集合的大括号.例如,在等式f(s,V-s)=f(s,V)中',
            '项V-s是指集合V-{s}')
        print('隐含集合记号常可以简化有关流的等式.下列引理给出了有关流和隐含记号的几个恒等式')
        print('引理26.1 设G=(V,E)是一个流网络,f是G中的一个流.那么下列等式成立')
        print(' 1) 对所有X∈V,f(X,X)=0')
        print(' 2) 对所有X,Y∈V,f(X,Y)=-f(Y,X)')
        print(' 3) 对所有X,Y,Z∈V,其中X∧Y!=None,有f(X∨Y,Z)=f(X,Y)+f(Y,Z)且f(Z,X∨Y)=f(Z,X)+f(Z,Y)')
        print('作为应用隐含求和记法的一个例子,可以证明一个流的值为进入汇点的全部网络流,即|f|=f(V,t)')
        print('根据流守恒特性,除了源点和汇点以外,对所有顶点来说,进入顶点的总的正流量等于离开该顶点的总的正能量',
            '根据定义,源点顶点总的净流量大于0；亦即，对源点顶点来说，离开它的正流要比进入它的正流更多',
            '对称地，汇点顶点是唯一一个其总的净流量小于0的顶点;亦即,进入它的正流要比离开它的正流更多')
        print('练习26.1-1 利用流的定义，证明如果(u,v)∉E,且(v,u)∉E,有f(u,v)=f(v,u)=0')
        print('练习26.1-2 证明：对于任意非源点非汇点的顶点v,进入v的总正向流必定等于离开v的总正向流')
        print('练习26.1-3 证明在具有多个源点和多个汇点的流网络中,任意流均对应于通过增加一个超级源点',
            '和超级汇点所得到的具有相同值的一个单源点单汇点流')
        print('练习26.1-4 证明引理26.1')
        print('练习26.1-5 在所示的流网络G=(V,E)和流f,找出两个子集合X,Y∈V,且满足f(X,Y)=-f(V-X,Y)',
            '再找出两个子集合X,Y∈V,且满足f(X,Y)!=-f(V-X,Y)')
        print('练习26.1-6 给定流网络G=(V,E),设f1和f2为V*V到R上的函数.流的和f1+f2是从V*V到R上的函数',
            '定义如下：对所有u,v∈V (f1+f2)(u,v)=f1(u,v)+f2(u,v)',
            '如果f1和f2为G的流,则f1+f2必满足流的三条性质中的哪一条')
        print('练习26.1-7 设f为网络中的一个流,a为实数。标量流之积是一个从V*V到R上的函数,定义为(af)(u,v)=a*f(u,v)',
            '证明网络中的流形成一个凸集','即证明如果f1和f2是流,则对所有0<=a<=1,af1+(1-a)f2也是流')
        print('练习26.1-8 将最大流问题表述为一个线性规划问题')
        print('练习26.1-9 略')
        # python src/chapter26/chapter26note.py
        # python3 src/chapter26/chapter26note.py

class Chapter26_2:
    '''
    chpater26.2 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter26.2 note

        Example
        ====
        ```python
        Chapter26_2().note()
        ```
        '''
        print('chapter26.2 note as follow')  
        # python src/chapter26/chapter26note.py
        # python3 src/chapter26/chapter26note.py

class Chapter26_3:
    '''
    chpater26.3 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter26.3 note

        Example
        ====
        ```python
        Chapter26_3().note()
        ```
        '''
        print('chapter26.3 note as follow')  
        # python src/chapter26/chapter26note.py
        # python3 src/chapter26/chapter26note.py

class Chapter26_4:
    '''
    chpater26.4 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter26.4 note

        Example
        ====
        ```python
        Chapter26_4().note()
        ```
        '''
        print('chapter26.4 note as follow')  
        # python src/chapter26/chapter26note.py
        # python3 src/chapter26/chapter26note.py

class Chapter26_5:
    '''
    chpater26.5 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter26.5 note

        Example
        ====
        ```python
        Chapter26_5().note()
        ```
        '''
        print('chapter26.5 note as follow')  
        # python src/chapter26/chapter26note.py
        # python3 src/chapter26/chapter26note.py

chapter26_1 = Chapter26_1()
chapter26_2 = Chapter26_2()
chapter26_3 = Chapter26_3()
chapter26_4 = Chapter26_4()
chapter26_5 = Chapter26_5()

def printchapter26note():
    '''
    print chapter26 note.
    '''
    print('Run main : single chapter twenty-six!')  
    chapter26_1.note()
    chapter26_2.note()
    chapter26_3.note()
    chapter26_4.note()
    chapter26_5.note()

# python src/chapter26/chapter26note.py
# python3 src/chapter26/chapter26note.py
if __name__ == '__main__':  
    printchapter26note()
else:
    pass
