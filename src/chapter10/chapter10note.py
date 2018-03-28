
# python src/chapter10/chapter10note.py
# python3 src/chapter10/chapter10note.py
'''
Class Chapter10_1

'''
import sys as _sys
import math as _math
import random as _random
import time as _time
from random import randint as _randint
from copy import copy as _copy, deepcopy as _deepcopy
from numpy import arange as _arange
import numpy as np

import numpy.fft as fft
from numpy import matrix


if __name__ == '__main__':
    import collection as c
else:
    from . import collection as c

class Chapter10_1:
    '''
    chpater10.1 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter10.1 note

        Example
        ====
        ```python
        Chapter10_1().note()
        ```
        '''
        print('chapter10.1 note as follow')
        print('第三部分 数据结构')
        print('如同在数学中一样，集合也是计算机科学的基础。不过数学中的集合是不变的')
        print('而算法所操作的集合却可以随着时间的改变而增大、缩小或产生其他变化。我们称这种集合是动态的')
        print('接下来的五章要介绍在计算机上表示和操纵又穷动态集合的一些基本技术')
        print('不同的算法可能需要对集合执行不同的操作。例如：许多算法只要求能将元素插入集合、从集合中删除元素以及测试元素是否属于集合')
        print('支持这些操作的动态集合成为字典')
        print('另一些算法需要一些更复杂的操作，例如第6章在介绍堆数据结构时引入了最小优先队列，它支持将一个元素插入一个集合')
        print('1.动态集合的元素')
        print(' 在动态集合的典型实现中，每个元素都由一个对象来表示，如果有指向对象的指针，就可以对对象的各个域进行检查和处理')
        print(' 某些动态集合事件假定所有的关键字都取自一个全序集，例如实数或所有按字母顺序排列的单词组成的集合')
        print(' 全序使我们可以定义集合中的最小元素，或确定比集合中已知元素大的下一个元素等')
        print('2.动态集合上的操作')
        print(' 操作可以分为两类：查询操作和修改操作')
        print(' Search(S, k); Insert(S, x); Delete(S, x); ')
        print(' Minimum(S); Maximum(S); Successor(S, x); Predecessor(S, x)')
        print('第10章 基本数据结构')
        print('很多复杂的数组局够可以用指针来构造，本章只介绍几种基本的结构，包括栈，队列，链表，以及有根树')
        print('10.1 栈和队列')
        print('栈和队列都是动态集合，在这种结构中，可以用delete操作去掉的元素是预先规定好的')
        print('栈实现一种后进先出LIFO的策略；队列实现了先进先出FIFO的策略')
        print('用作栈上的Insert操作称为压入Push，而无参数的Delete操作常称为弹出Pop')
        print('可以用一个数组S[1..n]来实现一个至多有n个元素的栈；数组S有个属性top[S],它指向最近插入的元素')
        print('由S实现的栈包含元素S[1..top[S]],其中S[1]是栈底元素,S[top[S]]是栈顶元素')
        print('当top[S]=0时，栈中不包含任何元素，因而是空的')
        print('要检查一个栈为空可以使用查询操作isEmpty,试图对一个空栈做弹出操作，则称栈下溢')
        print('如果top[S]超过了n，则称栈上溢')
        print('以上三种栈操作的时间均为O(1)')
        s = c.Stack()
        print(s.isEmpty())
        s.push('123')
        s.push(1)
        print(s.count())
        s.pop()
        print(s.pop(), s.count())
        print('队列：Innsert操作称为Enqueue;Delete操作称为Dequeue,队列具有FIFO性质')
        print('队列有头有尾，当元素入队时，将被排在队尾，出队的元素总为队首元素')
        print('用一个数组Q[1..n]实现一个队列，队列具有属性head[Q]指向队列的头，属性tail[Q]指向新元素会被插入的地方')
        print('当元素排列为一个环形时为环形队列，当队列为空时，试图删除一个元素会导致队列的下溢')
        print('当haed[Q]=tail[Q]+1时，队列是满的，这时如果插入一个元素会导致队列的上溢')
        q = c.Queue([1, 2, 3])
        print(q.length())
        q.enqueue(4)
        q.dequeue()
        print(q.array)
        s = c.Stack()
        s.push(4);s.push(1);s.push(3);s.pop();s.push(8);s.pop()      
        print('练习10.1-1: stack:', s.array)
        s = c.TwoStack()
        s.one_push(1)
        s.two_push(9)
        s.one_push(2)
        s.one_push(3)
        s.one_push(4)
        print('练习10.1-2: ')
        print(' ', s.one_all(), s.two_all())
        try:
            s.two_push(8)
        except Exception as err:
            print(' ', err)
        q = c.Queue()
        q.enqueue(4);q.enqueue(1);q.enqueue(3);q.dequeue();q.enqueue(8);q.dequeue()
        print('练习10.1-3: queue:', q.array)
        try:
            q = c.Queue()
            q.dequeue()
        except Exception as err:
            print('练习10.1-4: ')
        dq = c.DoubleQueue()
        dq.enqueue(1);dq.enqueue(2);dq.enqueue_reverse(3)
        print('练习10.1-5: 双端队列：', dq.array)
        q = c.QueueUsingStack()
        q.enqueue(1);q.enqueue(2);q.enqueue(3)
        print('练习10.1-6: ', q.dequeue(), q.dequeue(), q.dequeue())
        s = c.StackUsingQueue()
        s.push(1);s.push(2);s.push(3)
        print('练习10.1-7: ', s.pop(), s.pop(), s.pop())
        
        # python src/chapter10/chapter10note.py
        # python3 src/chapter10/chapter10note.py
class Chapter10_2:
    '''
    chpater10.2 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter10.2 note

        Example
        ====
        ```python
        Chapter10_2().note()
        ```
        '''
        print('chapter10.2 note as follow')
        print('10.2 链表')
        print('在链表这种数据结构中，各对象按照线性顺序排序')
        print('链表与数组不同,数组的线性序是由数组的下标决定的，而链表中的顺序是由各对象中的指针决定的')
        print('链表可以用来简单而灵活地表示动态集合，但效率可能不一定很高')
        print('双链表L的每一个元素都是一个对象，每个对象包含一个关键字域和两个指针域：next和prev,也可以包含一些其他的卫星数据')
        print('对链表中的某个元素x，next[x]指向链表中x的后继元素，而prev[x]则指向链表中x的前驱元素。')
        print('如果prev[x]=NIL,则元素x没有前驱结点，即它是链表的第一个元素，也就是头(head);')
        print('如果next(x)=NIL,则元素x没有后继结点，即它是链表的最后一个元素，也就是尾')
        print('属性head[L]指向表的第一个元素。如果head[L]=NIL,则该链表为空')
        print('一个链表可以呈现为好几种形式。它可以是单链接的或双链接的，已排序的或未排序的，环形的或非环形的')
        print('在本节余下的部分，假定所处理的链表都是无序的和双向链接的')
        print('链表的搜索操作：简单的线性查找方法')
        print('链表的插入：给定一个已经设置了关键字的新元素x，过程LIST-INSERT将x插到链表的前端')
        print('链表的删除：从链表L中删除一个元素x，它需要指向x的指针作为参数')
        print('但是，如果希望删除一个具有给定关键字的元素，则要先调用LIST-SEARCH过程，', 
            '因而在最坏情况下的时间为Θ(n)')
        print('哨兵(sentinel)是个哑(dummy)对象，可以简化边界条件')
        l = c.List()
        l.insert(1);l.insert(2);l.insert(3)     
        print('链表中的元素总和:', l.all(), l.head.value, 
            l.head.next.value, l.head.next.next.value, l.count())
        l.delete_bykey(0)
        print(l.all())
        l.delete_bykey(2)
        print(l.all())
        print('练习10.2-1: 动态集合上的操作INSERT能用一个单链表在O(1)时间内实现')
        s = c.StackUsingList()
        s.push(1);s.push(2);s.push(3);s.pop()
        print('练习10.2-2: ', s.all())
        q = c.QueueUsingList()
        q.enqueue(1);q.enqueue(2);q.enqueue(3);q.dequeue()
        print('练习10.2-3: ', q.all())
        print('练习10.2-4: 不用哨兵NIL就可以了')
        print('练习10.2-5: 用环形单链表来实现字典操作INSERT,DELETE和SEARCH，以及运行时间')
        print('练习10.2-6: 应该选用一种合适的表数据结构，以便之处在O(1)时间内的Union操作')
        print('练习10.2-7: 链表反转过程Θ(n)的非递归过程，对含有n个元素的单链表的链进行逆转')
        print(' 除了链表本身占用的空间外，该过程仅适用固定量的存储空间')
        print('练习10.2-8: 如何对每个元素仅用一个指针np[x](而不是两个指针next和prev)来实现双链表')
        print(' 假设所有指针值都是k位整型数，且定义np[x] = next[x] XOR prev[x],即next[x]和')
        print(' prev[x]的k位异或(Nil用0表示)。注意要说明访问表头所需的信息，以及如何实现在该表上的SEARCH,INSERT和DELETE操作')
        print(' 如何在O(1)时间内实现这样的表')
        # python src/chapter10/chapter10note.py
        # python3 src/chapter10/chapter10note.py

class Chapter10_3:
    '''
    chpater10.3 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter10.3 note

        Example
        ====
        ```python
        Chapter10_3().note()
        ```
        '''
        print('chapter10.3 note as follow')
        print('指针和对象的实现')
        print('有些语言(如FORTRAN)中不提供指针与对象数据类型')
        print('对象的多重数组表示')
        print(' 对一组具有相同域的对象，每一个域都可以用一个数组表示')
        print(' 动态结合现有的关键字存储在数组key，而指针存储在数组next和prev中')
        print(' 对于某一给定的数组下标x, key[x], next[x], prev[x]就共同表示链表中的一个对象')
        print(' 在这种解释下，一个指针x即为指向数组key, next, prev的共同下标')
        print(' 在给出的伪代码中，方括号既可以表示数组的下标，又可以表示对象的某个域(属性)')
        print(' 无论如何，key[x],next[x],prev[x]的含义都与实现是一致的')
        print('对象的单数组表示')
        print(' 计算机存储器中的字是用整数0到M-1来寻址的，此处M是个足够大的整数。')
        print(' 在许多程序设计语言中，一个对象占据存储中的一组连续位置，指针即指向某对象所占存储区的第一个位置，后续位置可以通过加上相应的偏移量进行寻址')
        print(' ')
        print('')
        # python src/chapter10/chapter10note.py
        # python3 src/chapter10/chapter10note.py

chapter10_1 = Chapter10_1()
chapter10_2 = Chapter10_2()
chapter10_3 = Chapter10_3()

def printchapter10note():
    '''
    print chapter10 note.
    '''
    print('Run main : single chapter ten!')  
    chapter10_1.note()
    chapter10_2.note()
    chapter10_3.note()

# python src/chapter10/chapter10note.py
# python3 src/chapter10/chapter10note.py
if __name__ == '__main__':  
    printchapter10note()
else:
    pass
