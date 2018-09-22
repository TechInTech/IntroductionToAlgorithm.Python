# coding:utf-8
# usr/bin/python3
# python src/chapter33/chapter33note.py
# python3 src/chapter33/chapter33note.py
"""

Class Chapter33_1

Class Chapter33_2

Class Chapter33_3

Class Chapter33_4

"""
from __future__ import absolute_import, division, print_function

if __name__ == '__main__':
    pass
else:
    pass

class Chapter33_1:
    """
    chapter33.1 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter33.1 note

        Example
        ====
        ```python
        Chapter33_1().note()
        ```
        """
        print('chapter33.1 note as follow')
        print('第33章 计算几何学')
        print('计算几何学问题的输入一般是关于一组几何对象的描述,如一组点、一组线段,或者一个多边形的按逆时针顺序排列的一组顶点')
        print('输出常常是对有关这些对象的问题的回答,如是否直线相交,是否为一个新的几何对象,如顶点集合的凸包(convex hull,即最小封闭多边形)')
        print('本章中,将学习一些二维的(即平面上的)计算几何学算法,在这些算法中,每个输入对象都用一组点{p1,p2,p3,...}来表示,其中每个pi=(xi,yi)',
            'xi,yi∈R.例如：一个顶点的多边形P可以用一组点<p0,p1,p2,...,pn-1>来表示,这些点按照在P的边界上出现的顺序排列.')
        print('计算几何学也可以用来求解三维空间,甚至高维空间中的问题,但这样的问题及其解决方案是很难视觉化的')
        print('不过,即使是在二维平面上,也能够看到应用计算几何学技术的一些很好的例子')
        print('33.1节说明如何有效地准确回答有关线段的一些基本问题：一条线段是在与其共享一个端点的另一条线段的顺时针方向，还是在其逆时针方向')
        print('33.2节介绍一种称为“扫除”的技术，利用该技术设计一种运行时间为O(nlgn)的算法,用来确定n条线段中是否包含相交的线段')
        print('33.3节给出两种“旋转扫除”的算法，用于计算n个点的凸包(最小封闭的凸多边形)。这两个算法分别是运行时间为O(nlgn)的Graham扫描法和运行时间为O(nh)的Jarvis步进法(h是凸包中顶点的数目)')
        print('33.4节介绍一种运行时间为O(nlgn)的分治算法,用于在平面上的n个点中找出距离最近的一个点对')
        print('33.1 线段的性质')
        print('两个不同的点p1=(x1,y1)和p2=(x2,y2)的凸组合是满足下列条件的任意点p3=(x3,y3):对某个a,(0<=a<=1),有x3=ax1+(1-a)y2.',
            '也可以写作p3=ap1+(1-a)p2,从直观上看,p3是位于p1和p2的直线上、并处于p1和p2之间的凸组合的集合.我们称p1和p2为线段p1p2的端点。有时,还要考虑到p1和p2之间的顺序,这时,可以说有向线段p1p2',
            '如果p1是原点(0,0),则可以把有向线段p1p2看作向量p2')
        print('本节即将讨论以下问题')
        print('  (1)已知两条有向线段p0p1和p0p2,相对于它们的公共端点p0来说,p0p1是否在p0p2的顺时针方向上？')
        print('  (2)已知两条线段p0p1和p1p2,如果先通过p0p1再通过p1p2,在点p1处是不是要向左旋转')
        print('  (3)线段p1p2和p3p4是否相交')
        print('可以在O(1)时间内回答以上每个问题,这一点不会使人惊讶,因为每个问题的输入规模都是O(1),此外,将采用的方法仅限于加法、减法和比较运算',
            '既不需要除法运算，也不需要三角函数，这两者的计算代价都比较高昂,并且容易产生舍入误差等问题')
        print('例如要确定两条线段是否相交,一种直接的方法就是对这两条线段,都计算出形如y=mx+b的直线方程(其中m为斜率,b为y轴截距),找出两条直线的交点,',
            '并检查交点是否同时在两条线段上,在这一方法中,用除法求出交点.当线段接近于平行时,算法对实际计算机中除法运算的精度非常敏感',
            '本节中的方法避免使用除法,因而要精确的多')
        print('叉积')
        print('  叉积(cross product)的计算是关于线段算法的中心。向量p1和p2可以把叉积p1×p2看做是由点(0,0),p1,p2和p1+p2=(x1+x2,y1+y2)',
            '所形成的平行四边形的面积。另一种等价而更有用的定义是把叉积定义为一个矩阵的行列式',
            'p1×p2=det[[x1 x2],[y1 y2]]=x1y2-x2y1=-p2×p1')
        print('  如果p1×p2为正数,则相对于原点(0,0)来说,p1在p2在顺时针方向上;如果p1×p2为负数,则p1在p2的逆时针方向上')
        print('  为了确定相对于公共端点p0,有向线段p0p1是否在有向线段p0p2的顺时针方向,只需要把p0作为原点就可以了。亦即,可以用p1-p0表示向量p1’=(x1‘,y1’),其中x1‘=x1-x0,',
            'y1’=y1-y0.类似地可以定义p2-p0,然后计算叉积:',
            '(p1-p0)×(p2-p0)=(x1-x0)(y2-y0)-(x2-x0)(y1-y0)',
            '如果该叉积为正,则p0p1在p0p2的顺时针方向上;如果为负,则p0p1在p0p2的逆时针方向上')
        print('确定连续线段是向左转还是向右转')
        print('  在点p1处,两条连续的线段p0p1和p1p2是向左转还是向右转。亦即,希望找出一种方法,以确定一个给定的角∠p0p1p2的转向.运用叉积,',
            '使得无需对角进行计算,就可以回答这个问题.只需要检查一下有向线段p0p2是在有向线段p0p1的顺时针方向,还是在其逆时针方向.',
            '还是在其逆时针方向.在做这一判断时,要计算出叉积(p2-p0)×(p1-p0).如果该叉积的符号为负,则p0p2在p0p1的逆时针方向,因此,在p1点要向左转.',
            '如果叉积为正,就说明p0p2在p0p1的顺时针方向,因此,在点p1处要向右转。叉积为0说明点p0,p1和p2共线')
        print('确定两个线段是否相交')
        print('  为了确定两个线段是否相交,要检查每个线段是否跨越了包含另一线段的直线,给定一个线段p1p2,如果点p1位于某一直线的一边,而点p2位于该直线的另一边',
            '则称线段p1p2跨越了该直线.如果p1和p2就落在该直线上的话,即出现边界情况.两个线段相交,当且仅当下面两个条件中有一个成立,或同时成立')
        print('  (1) 每个线段都跨越包含了另一线段的直线')
        print('  (2) 一个线段的某一端点位于另一线段上.')
        print('叉积的其他应用')
        print('  33.3节中,根据相对于某一顶点原点的极角大小来对一组点进行排序')
        print('  33.2节中,运用红黑树来保持一组线段的垂直顺序。在这种方法中,',
            '并不是显式地记录关键字值,而是将红黑树代码中的每一次关键字值比较替换为叉积计算,以便确定与某指定垂直直线相交额两条线段中,相互的上下顺序')
        print('练习33.1-1 证明：如果p1*p2为正,则相对于原点(0,0),向量p1在向量p2的顺时针方向；如果叉积为负,则p1在p2的逆时针方向')
        print('练习33.1-2 略')
        print('练习33.1-3 一个点p1相对于原点p0的极角(polar angle)即在常规的极坐标系统中,向量p1-p0的极角.例如,相对于(2,4)而言,点(3,5)的极角即为向量(1,1)的极角',
            '即45度或Pi/4弧度.相对于(2,4)而言,(3,3)的极角为向量(1,-1)的极角,即315度或7Pi/4弧度.请编写一段伪代码,根据相对于某个给定原点p0的极角',
            '对一个由n点组成的序列<p1,p2,...,pn>进行排序.所给出过程的运行时间应为O(nlgn),并要求用叉积来比较极角的大小')
        print('练习33.1-4 试说明如何在O(n^2lgn)的时间内,确定n个点中的任意三点是否共线')                                     
        print('练习33.1-5 多边形(polygon)是平面上由一系列线段构成的、封闭的曲线。亦即，它是一条首尾相连的曲线，由一系列直线段所形成',
            '这些直线段称为多边形的边(side).一个连接了两条连续边的点称为多边形的顶点。如果多边形是简单的(一般情况下都会作此假设),',
            '它自身内部不会发生交叉。在平面上,由一个简单的多边形包围的一组点形成了该多边形的所有点则形成了其外部')
        print('练习33.1-6 已知一个点p0=(x0,y0),p0的右水平射线是点的集合{pi=(xi,yi):xi>=x0,且yi=y0},亦即,它是p0点正右方的点的集合,包含p0本身',
            '试说明如何通过把问题转换为确定两条线段是否相交的问题,从而可以在O(1)的时间内,确定给定的p0的右水平射线是否与线段p1p2相交')
        print('练习33.1-7 要确定一个点p0是否在一个简单多边形P(不一定是凸多边形)内部,一种方法是检查由p0发出的任何射线,看它是否与多边形P的边界相交奇数次',
            '但p0本身不能处于P的边界上.试说明如何在Θ(n)的时间内,计算出点p0是否在一个由n个顶点组成的多边形P的内部')
        print('练习33.1-8 试说明如何在Θ(n)的时间内,计算出由n个顶点所组成的简单多边形(但不一定是凸多边形)的面积')
        # python src/chapter33/chapter33note.py
        # python3 src/chapter33/chapter33note.py

class Chapter33_2:
    """
    chapter33.2 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter33.2 note

        Example
        ====
        ```python
        Chapter33_2().note()
        ```
        """
        print('chapter33.2 note as follow')
        print('33.2 确定任意一对线段是否相交')
        print('一组线段中任意两条线段是否相交的扫除技术,这种技术或其变体许多几何学算法都用到')
        print('该算法的运行时间为O(nlgn),其中n是已知线段的数目，它仅确定是否存在相交的线段,但并不输出所有的相交的线段')
        print('最坏情况下，要找出n个线段中的所有相交点，所需的时间为Ω(n^2)')
        print('在扫除过程中，一条假想的的垂直扫除线穿过已知的几何物体,并且通常是从左到右依次移动扫除线.',
            '扫除线移动的空间方向可以看作是一种时间上先后顺序的度量')
        print('扫除技术提供了一种对一组几何物体进行排序的方法,通常先把它们放入一个动态数据结构中,并且利用它们之间的关系对其进行排序.',
            '本节中确定线段相交的算法按从左到右的次序考察所有的线段端点,每遇到一个端点就检查是否是相交点')
        print('为了描述确定n条线段中任意两条是否相交的算法并证明其正确性,做出了如下两条简化性假设:第一,假定没有一条输入线段是垂直的.',
            '第二,假定没有三条输入线段相交于同一点.即使这两条假设不成立,算法也能正常的工作.的确,如果去掉上面的两条简化性假设后',
            '在为计算几何学算法编程并证明其正确性时,对边界条件的处理就常常是最棘手的部分了')
        print('排序线段')
        print('  假定不存在垂直线段,所以任何与给定垂直扫除线相交的输入线段与其只能有一个交点.因此,可以根据交点的y坐标对与给定垂直扫除线相交的线段进行排序')
        print('  更准确地说,考察两条线段s1和s2.如果一条横坐标为x的垂直扫除线与这两条线段都相交,则说两条线段在x是可比的',
            '如果s1和s2在x处是可比的,并且在x处,s1与扫除线的交点比s2与同一条扫除线的交点高,则说在x处s1位于s2之上,写作s1>xs2')
        # !扫除算法
        print('扫除线的移动')
        print('  典型的扫除算法要维护下列的两组数据')
        print('  (1) 扫除线状态：给出了与扫除线相交的物体之间的关系')
        print('  (2) 事件点调度：是一个从左向右排列的x坐标的序列,它定义了扫除线的暂停位置。',
            '称每个这样的暂停位置为事件点。扫除线状态仅在事件点处才会发生变化')
        print('对于某些算法,事件点调度是随算法执行而动态地确定的.现在讨论的算法仅是基于输入数据的简单性质静态地确定事件点。',
            '特别地,每条线段的端点都是事件点.通过增加x坐标,并从左向右执行来对线段的端点进行排序',
            '当遇到线段的左端点时,就把该线段插入到扫除线状态中,并且当遇到其右端点时,就把它从扫除线状态中删除.',
            '当每两条线段在全序中第一次变为连续时,就检查它们是否相交')
        print('扫除线状态是一个全序T,在T上要执行下列操作:')
        print('(1) INSERT(T, s): 把线段s插入到T中')
        print('(2) DELETE(T, s): 把线段s从T中删除')
        print('(3) ABOVE(T, s): 返回T中紧靠线段s上面的线段')
        print('(4) BELOW(T, s): 返回T中紧靠线段s下面的线段')
        print('如果输入中有n条线段,则可以运用红黑树,在O(lgn)时间内执行上述每个操作.读者可以回顾一下',
            '红黑树操作涉及了关键字的比较','此处可以用叉积比较来取代关键字比较,以确定两个线段的相对次序')
        print('求线段交点的伪代码')
        print('ANY-SEGMENTS-INTERSECT(S)下列算法的输入是由n个线段组成的集合S,如果S中的任何一对线段相交,',
            '算法就返回布尔值TRUE,否则就返回就FALSE.全序T是由是由一棵红黑树来实现的')
        print('正确性')
        print('  证明当且仅当S中的线段有一个交点时,对ANY-SEGMENTS-INTERSECT(S)的调用返回TRUE')
        print('运行时间')
        print('  如果集合S中有n条线段,则ANY-SEGMENTS-INTERSECT的运行时间为O(nlgn),',
            '则可以使每次相交测试所需的时间为O(1).因此,总的运行时间为O(nlgn)')
        print('练习33.2-1 证明:在n条线段的集合中,可能有Θ(n^2)个交点')
        print('练习33.2-2 已知两条在x处可比的线段a和b,式说明如何在O(1)时间内确定a>xb和b>xa中哪一个成立.假定这两条线段都不是垂直的',
            '(提示：如果a和b不相交,仍然可以只利用加、减、乘这几种运算，无需用除法.当然,在应用>x关系时,如果a和b相交,就可以停下来并声明找到了一个交点)')
        print('练习33.2-3 Maginot教授建议修改过程ANY-SEGMENTS-INTERSECT,使其不是找出一个交点后就返回,而是输出相交的线段,',
            '再继续进行for循环的下一次迭代.称这样得到的过程为PRINT-INTERSECTING-SEGMENTS,并声称该过程能够安札线段在集合中出现的次序',
            '从左到右输出所有的交点.试着说明这位教授的说法有两点是错误的,即举出一组线段,使得运用过程PRINT-INTERSECTING-SEGMENTS所找出的一个相交点不是最左相交点',
            '再举出出一组线段,使过程PRINT-INTERSECGING-SEGMENTS不能找出所有的相交点')
        print('练习33.2-4 写出一个运行时间为O(nlgn)的算法,以确定由n个顶点组成的多边形是否是简单多边形')
        print('练习33.2-5 写出一个运行时间为O(nlgn)的算法,以确定总共有n个顶点的两个简单多边形是否相交')
        print('练习33.2-6 一个圆面是由一个圆加上其内部所组成,并且用圆心和半径表示。如果两个圆面有任何公共点',
            '则称这两个圆面相交。写出一个运行时间为O(nlgn)的算法,一确定n个圆面中是否有任何两个圆面相交')
        print('练习33.2-7 已知n条线段中总共包含k个交点,式说明如何在O((n+k)lgn)时间内,输出全部k个交点')
        print('练习33.2-8 论证即使有三条或更多的线段相交于同一点,过程ANY-SEGMENTS-INTERSECT也能正确执行')
        print('练习33.2-9 证明在有垂直线段的情况下,如果某一垂直线段的底部端点被当做是左端点来处理,其顶部端点被当做是右端点来处理,',
            '则过程ANY-SEGMENTS-INTERSECT也能正确执行.如果允许有垂直线段的话')
        # python src/chapter33/chapter33note.py
        # python3 src/chapter33/chapter33note.py

class Chapter33_3:
    """
    chapter33.3 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter33.3 note

        Example
        ====
        ```python
        Chapter33_3().note()
        ```
        """
        print('chapter33.3 note as follow')
        print('33.3 寻找凸包')
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
        print('')
        print('')
        print('')
        print('')
        # python src/chapter33/chapter33note.py
        # python3 src/chapter33/chapter33note.py

class Chapter33_4:
    """
    chapter33.4 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter33.4 note

        Example
        ====
        ```python
        Chapter33_4().note()
        ```
        """
        print('chapter33.4 note as follow')
        # python src/chapter33/chapter33note.py
        # python3 src/chapter33/chapter33note.py

chapter33_1 = Chapter33_1()
chapter33_2 = Chapter33_2()
chapter33_3 = Chapter33_3()
chapter33_4 = Chapter33_4()

def printchapter33note():
    """
    print chapter33 note.
    """
    print('Run main : single chapter thirty-three!')
    chapter33_1.note()
    chapter33_2.note()
    chapter33_3.note()
    chapter33_4.note()

# python src/chapter33/chapter33note.py
# python3 src/chapter33/chapter33note.py

if __name__ == '__main__':  
    printchapter33note()
else:
    pass
