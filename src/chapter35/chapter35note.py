# coding:utf-8
# usr/bin/python3
# python src/chapter35/chapter35note.py
# python3 src/chapter35/chapter35note.py
"""

Class Chapter35_1

Class Chapter35_2

Class Chapter35_3

Class Chapter35_4

Class Chapter35_5

"""
from __future__ import absolute_import, division, print_function

if __name__ == '__main__':
    pass
else:
    pass

class Chapter35_1:
    """
    chapter35.1 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter35.1 note

        Example
        ====
        ```python
        Chapter35_1().note()
        ```
        """
        print('chapter35.1 note as follow')
        print('第35章 近似算法')
        print('许多具有实际意义的问题都是NP完全问题,但都非常重要,所以不能仅因为获得其最优解的过程非常困难就放弃')
        print('解决NP完全问题至少有三种方法:第一,如果实际输入的规模比较小,则用具有指数运行时间的算法来解决问题就很理想了.',
            '第二,或许能将一些重要的、多项式时间可解的特殊情况隔离出来;第三,仍有可能在多项式时间里面找到(最坏情况或平均情况)近似最优解.',
            '在实践中,近似最优解常常就足够好了,就返回近似最优解的算法称为近似算法')
        print('近似算法的性能比值')
        print('假定在解一个最优化问题,该问题的每一个可能解都有正的代价,希望找出一个近似最优解.根据所要解决的问题',
            '最优解可以定义成具有最大可能代价的解或具有最小可能代价的解.就是说,该问题可能是一个求最大值的问题或求最小值的问题')
        print('说问题的一个近似算法有着近似比p(n),如果对规模为n的任何输入,由该近似算法产生的解的代价C与最优解的代价C*只差一个因子p(n)',
            'max(C/C*,C*/C)<=p(n),也称一个能达到近似比p(n)的算法为p(n)近似算法.这个定义对求最大值和求最小值问题都适用.',
            '对于一个求最大值的问题,0<C<=C*,而比值C*/C给出最优解的代价大于近似解的代价的倍数.类似地,对于求最小值问题也是同理')
        print('对于很多问题来说,已经设计出具有较小的固定近似比的多项式时间近似算法;对于另一些问题来说,在其已知的最佳多项式时间的近似算法中,',
            '近似比是作为输入规模n的函数而增长的')
        print('一些NP完全问题允许有多项式时间的近似算法,通过消耗越来越多的计算时间,这些近似算法可以达到不断缩小的近似比.就是说,在计算时间和近似的质量之间可以进行权衡')
        print('一个最优化问题的近似方案是这样的一种近似算法,它的输入除了该问题的实例外,还有一个值e>0,使得对任何固定的e,该方案是个(1+e)近似算法',
            '对一个近似方案来说,如果对任何固定的e>0,该方案都以其输入实例的规模n的多项式时间运行,则称此方案为多项式时间近似方案')
        print('随着e的减小,多项式时间近似方案的运行时间会迅速增长.例如,一个多项式时间近似方案的运行时间可能达到O(n^2/e).在理想情况下,',
            '如果e按一个常数因子减小,为了获得希望的近似效果,所增加的运行时间不应该超过一个常数因子.',
            '希望运行时间既是1/e的多项式,又是n的多项式')
        print('对一个近似方案来说,如果其运行时间既是1/e的多项式,又为输入实例的规模n的多项式,则称其为完全多项式时间的近似方案.',
            '例如,近似方案可能有O((1/e)^2n^3)运行时间.对于这样的一种方案,e的任意常数倍的减少可以由运行时间的相应常数倍增加来弥补')
        print('35.1 顶点覆盖问题')
        print('虽然在一个图G中寻找最优顶点覆盖比较困难,但要找出一个近似最优的顶点覆盖不会太难.下面给出的近似算法以一个无向图G为输入,',
            '并返回一个其规模保证不超过最优顶点覆盖的规模两倍的顶点覆盖规模两倍的顶点覆盖')
        print('定理35.1 APPROX-VERTEX-COVER有一个多项式时间的2近似算法')
        print('练习35.1-1 给出一个图的例子,使得APPROX-VERTEX-COVER对该图总是产生次最优解')
        print('练习35.1-2 设A表示在APPROX-VERTEX-COVER的第4行中挑选出来的边集.证明:集合A是图G中的一个最大匹配')
        print('练习35.1-3 Nixon教授提出了以下的启发式方法来解决顶点覆盖问题:重复地选择度数最高的顶点并去掉所有邻接边.给出一个例子,',
            '说明这位教授的启发式方法达不到近似比2(提出:可以考虑一个二分图,其中左图中的顶点的度数一样,而右图中顶点的度数不一样)')
        print('练习35.1-4 给出一个有效的贪心算法,以便在线性时间内,找出一棵树的最优顶点覆盖')
        print('练习35.1-5 顶点覆盖问题和NP完全团问题在某种意义上来说是互补的,即最优顶点覆盖是补图中某一最大规模团的补.',
            '这种关系是否意味着存在着一个多项式时间的近似算法,它对团问题有着固定的近似比?请给出你的回答,并对你的回答加以说明')
        # python src/chapter35/chapter35note.py
        # python3 src/chapter35/chapter35note.py

class Chapter35_2:
    """
    chapter35.2 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter35.2 note

        Example
        ====
        ```python
        Chapter35_2().note()
        ```
        """
        print('chapter35.2 note as follow')
        print('35.2 旅行商问题')
        print('给定一个完全的无向图G=(V,E),其中每条边(u,v)∈E都有一个非负的整数代价c(u,v),希望找出G的一个具有最小代价的哈密顿回路.')
        print('在很多实际情况中,从一个地方u直接到另一个地方w总是代价最小的.经由任何一个中转站v的一种路径不可能具有更小的代价了.',
            '换句话说,去掉一个中间站绝不会增加代价.将这一概念加以形式化,即如果对所有的顶点u,v,w∈V,有:c(u,w)<=c(u,v)+c(v,w)',
            '就称代价函数c满足三角不等式c(u,w)<=c(u,v)+c(v,w)就称代价函数c满足三角不等式')
        print('三角不等式是个很自然的不等式,在许多应用中,都能自动得到满足.例如:如果图的顶点为平面上的点,',
            '且在两个顶点之间旅行的代价即为它们之间通常的欧几里得距离,就满足三角不等式')
        print('即使强行要求代价函数满足三角不等式,也不能改变旅行商问题的NP完全性.',
            '因此,不可能找出一个准确解决这个问题的多项式时间算法,因而就要寻找一些好的近似算法')
        print('在35.2.1节中要讨论一个2近似算法,用于解决符合三角不等式的旅行商问题.在35.2.2节中,要证明如果不符合三角不等式,',
            '则不存在具有常数近似比多项式时间的近似算法,除非P=NP')
        print('35.2.1 满足三角不等式的旅行商问题')
        print('利用前一小节的方法,首先计算出一个结构(即最小生成树),其权值是最优旅行商路线长度的下界.接着,要利用这一最小生成树来生成一条遍历线路',
            '其代价不大于最小生成树权值的两倍,只要代价函数满足三角不等式即可')
        print('即使是采用MST-PRISM的简单实现,APPROX-TSP-TOUR的运行时间也是Θ(V^2).现在我们来证明：如果旅行商问题的某一实例的代价函数满足三角不等式,',
            'APPROX-TSP-TOUR所返回的游程的代价不大于最优游程的代价的两倍')
        print('定理35.2 APPROX-TSP-TOUR是一个解决满足三角不等式的旅行商问题的、多项式时间的2近似算法')
        print('  证明:前面已经证明了APPROX-TSP-TOUR的运行时间为多项式')
        print('35.2.2 一般旅行商问题')
        print('如果去掉关于代价函数c满足三角不等式的假设,则不可能在多项式时间内找到好的近似路线,除非N=NP')
        print('定理35.3 如果P!=NP则对任何常数p>=1,一般旅行商问题不存在具有近似比p的多项式时间近似算法')
        print('练习35.2-1 假设有一个完全无向图G=(V,E),含有至少三个顶点,其代价函数c满足三角不等式.证明:对所有的u,v∈V,有c(u,v)>=0')
        print('练习35.2-2 说明如何才能在多项式时间内,将旅行商问题的一个实例转换为另一个其代价函数满足三角不等式的实例.',
            '两个实例必须有同一组最优游程.请解释为什么这样的一种多项式时间的转换与定理35.3并不矛盾,假设P!=NP.')
        print('练习35.2-3 考虑以下的用于构造近似旅行商游程的最近点启发式:从只包含任意选择的某一顶点的平凡回路开始.',
            '在每一步中,找出一个顶点u,它不在回路中,但与回路上任何顶点之间的距离最短.假设回路上距离u最近的顶点为v.将回路加以扩展以包含顶点u,即将u插入在v之后',
            '重复这一过程,直到所有的顶点都在回路上时为止.证明：这一启发式返回的游程总代价不大于最优游程代价的两倍')
        print('练习35.2-4 在瓶颈旅行商问题中,要找出这样的一条哈密顿回路,使得回路中代价最大的边的代价最小.假设代价函数满足三角不等式,',
            '证明：这个问题存在着一个近似比为3的多项式时间近似算法(采用递归证明的方法,通过完全遍历瓶颈生成树及跳过某些顶点,可以恰访问书中的每个顶点一次),',
            '但连续跳过的中间顶点不会多余两个.证明在瓶颈生成树中,代价最大的边的代价至多为瓶颈哈密顿葫芦中代价最大的边的代价')
        print('练习35.2-5 假设与旅行商问题的一个实例对应的顶点是平面上的点,且代价c(u,v)是点u和v之间的欧几里得距离.证明:一条最优游程不会自我交叉')
        # python src/chapter35/chapter35note.py
        # python3 src/chapter35/chapter35note.py

class Chapter35_3:
    """
    chapter35.3 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter35.3 note

        Example
        ====
        ```python
        Chapter35_3().note()
        ```
        """
        print('chapter35.3 note as follow')
        print('35.3 集合覆盖问题')
        print('集合覆盖问题是一个最优化问题,它模型化了许多资源选择问题,其相应的判定问题推广了NP完全的顶点覆盖问题,因而也是NP难度的.',
            '然而,用于解决顶点覆盖的近似算法在这儿就用不上了,需要尝试其他的一些方法.','要讨论一种简单的带对数近似比的贪心启发式方法,',
            '亦即,随着实例规模逐渐增大,相对于一个最优解的规模来说,近似解的规模也可能增大.但是,由于对数函数增长很慢,故这个近似算法可能会产生出很有用的结果来',
            '集合覆盖问题的一个实例(X,F)由一个有穷集合X和一个X的子集族F构成,且X的每一个元素属于F中的至少一个子集X=(S∈F)∪S')
        print('集合覆盖问题是对许多常见的组合问题的一种抽象.来看一个简单的例子：假设X表示解决某一问题所需要的各种技巧的集合,另外有一个给定的可用来解决该问题的人的集合.')
        print('一个贪心的近似算法')
        print('贪心方法在每一阶段都选择出能覆盖最多的、未被覆盖的元素的集合S(GREEDY-SET-COVER)')
        print('GREEDY-SET-COVER算法的工作过程是这样的,在每个阶段,集合U包含余下的未被覆盖的元素构成的集合；集合C包含正在被构造的覆盖.',
            '贪心决策步骤：即选出一个子集S,它能覆盖尽可能多的未被覆盖的元素(如果有两个子集覆盖了一样多的元素,可以任意选择其中的一个).',
            '在S被选出后,将其元素从U中去掉,b并将S置于C中.当该算法结束时,集合C就包含了一个覆盖X的F子族')
        print('GREEDY-SET-COVER算法存在一个运行时间为O(|X||F|min(|X|,|F|))的实现.')
        print('下面来证明以上的贪心算法可以返回一个比最优集合覆盖大不了很多的集合覆盖.为方便起见,在本章中,用H(d)来表示第d级调和数Hd=∑1/i',
            '作为一个边界条件,定义H(0)=0')
        print('定理35.4 GREEDY-SET-COVER是一个多项式时间的p(n)近似算法,其中p(n)=H(max{|S|:S∈F})')
        print('证明:已经证明了GREEDY-SET-COVER是以多项式时间运行的')
        print('推论35.5 GREEDY-SET-COVER是一个多项式时间的(ln|X|+1)近似算法')
        print('在某些应用中,max{|S|,S∈F}是一个较小的常数,在这种情况下,由GREEDY-SET-COVER返回的解就至多比最优解大一个很小的常数倍.',
            '例如,对一个其顶点的度至多为3的图来说,当利用这种启发式来获取其近似顶点覆盖时,即会出现这样的应用.',
            '在这种情况下,由GREEDY-SET-COVER找出的解不大于一个最优解的H(3)=11/6倍,这个性能保证比APPROX-VERTEX-COVER的要略好一些')
        print('练习35.3-1 将以下的每一个单词都看作是字母的集合:{arid,dash,drain,heard,lost,nose,shun,slate,snare,thread}.',
            '说明当出现两个候选集合可供选择时,如果倾向于在词典中先出现的单词,则GREEDY-SET-COVER会产生怎样的集合覆盖')
        print('练习35.3-2 通过从顶点覆盖问题进行归约,证明集合覆盖问题的判定版本是NP完全的')
        print('练习35.3-3 说明如何实现GREEDY-SET-COVER,使其运行时间为O(∑|S|)')
        print('练习35.3-4 以下给出的是定理35.4的较弱一些形式,证明它是成立的:|C|<=|C*|max{|S|:S∈F}')
        print('练习35.3-5 GREEDY-SET-COVER可以返回一些不同的解')
        # python src/chapter35/chapter35note.py
        # python3 src/chapter35/chapter35note.py

class Chapter35_4:
    """
    chapter35.4 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter35.4 note

        Example
        ====
        ```python
        Chapter35_4().note()
        ```
        """
        print('chapter35.4 note as follow')
        print('35.4 随机化和线性规划')
        print('给出3-CNF可满足性的最优化版本的一个随机化算法,还要利用线性规划,为顶点覆盖问题的一个带权版本设计近似算法.')
        print('解决MAX-3-CNF可满足性问题的一个随机化近似算法')
        print('正如存在着可以计算出准确解的随机算法一样,也存在着能够计算近似解的随机化算法.',
            '称某一问题的一个随机化算法具有近似比p(n),如果对任何规模为n的输入,该随机化算法所产生的解的期望代价C是在最优解的代价C*的一个因子p(n)之内:')
        print('  max(C/C*,C*/C)<=p(n)')
        print('能达到近似比p(n)的随机化算法也称为随机化的p(n)近似算法.换句话说,随机化的近似算法类似于确定型算法,只是其近似比的一个期望值')
        print('亦即,希望找出变量的一种赋值,使得有尽可能的子句得到满足.称这种最大化问题为MAX-3-CNF-可满足性问题的一种赋值,它能最大化结果为1的子句的数量.')
        print('定理35.6 给定MAX-3-CNF可满足性问题的一个实例,有n个变量x1,x2,...,xn和m个子句,',
            '以概率1/2独立地将每个变量设置为1和以概率1/2独立地将每个变量设置为0的随机化近似算法是一个随机化的8/7近似算法')
        print('利用线性规划来近似带权顶点覆盖')
        print('  在最小权值顶点覆盖问题,给定一个无向图G=(V,E),其中每个顶点v∈V都有一个关联的正的权值w(v).对任意顶点覆盖V\'∈V,',
            '定义该顶点覆盖的权为w(V‘)=∑w(v).目标是找出一个具有最小权值的顶点覆盖')
        print('  假设对每一个顶点v∈V,都安排一个变量x(v)与之关联,并且,要求对每一个顶点v∈V,有x(v)∈[0,1].',
            '将x(v)=1解释为v在顶点覆盖中,将x(v)=0解释为v不在顶点覆盖中.写出这样一条限制,即对于任意边(u,v),u和v之中至少有一个必须在顶点覆盖中',
            '即x(u)+x(v)>=1.这样一来,就引出了以下的用于寻找最小权值顶点覆盖的0-1整数规划')
        print('于是,线性规划的一个最优解是0-1整数规划最优解的一个下界,从而也是最小权值顶点覆盖问题最优解的下界')
        print('APPROX-MIN-WEIGHT-VC过程利用上述线性规划的解,构造最小权值顶点覆盖问题的一个近似解')
        print('定理35.7 APPROX-MIN-WEIGHT-VC是解决最小权值顶点覆盖问题的一个多项式时间的2近似算法')
        print('练习35.4-1 证明:即使允许一个子句既包含变量又包含其否定形式,将每个变量随机地以概率1/2设置为1和以概率1/2设置为0,它仍然是一个随机化的8/7近似算法')
        print('练习35.4-2 MAX-CNF可满足性问题与MAX-3-CNF可满足性问题类似,只是它并不限制每个子句都包含3个问题.',
            '对MAX-CNF可满足性问题,给出它的一个随机化的2近似算法')
        print('练习35.4-3 在MAX-CUT问题中,给定一个无权无向图G=(V,E).定义一个割(S,V-S),并定义一个割的权为通过该割的边的数目.',
            '问题的目标是找出一个具有最大权值的割.假设对每个顶点v,随机地且独立地将v以概率1/2置入S中,以概率1/2置入V-S中.证明:这个算法是一个随机化的2近似算法')
        print('练习35.4-4 略')
        # python src/chapter35/chapter35note.py
        # python3 src/chapter35/chapter35note.py

class Chapter35_5:
    """
    chapter35.5 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter35.5 note

        Example
        ====
        ```python
        Chapter35_5().note()
        ```
        """
        print('chapter35.5 note as follow')
        print('35.5 子集和问题')
        print('子集和问题的一个实例是一个对(S,t),其中S是一个正整数集合{x1,x2,...,xn},t为一个正整数.这个判定问题是判定是否存在S的一个子集,',
            '使得其中的数加起来恰为目标值t.这个问题是NP完全的')
        print('与此判定问题相联系的最优化问题常常出现于实际应用中,在这种最优化问题中,希望找到{x1,x2,...,xn}的一个子集,使其中元素相加之和尽可能的大,但不能大于t',
            '例如,假设有一辆能装不多于t磅重的货的卡车,并有n个不同的盒子要装运,其中第i个的重量为xi磅,希望在不超过重量极限的前提下,将货尽可能地装满卡车.')
        print('先给出解决这个最优化问题的一个指数时间算法,然后说明如何来修改算法,使之成为一个完全多项式时间的近似方案.',
            '(一个完全多项式时间近似方案的运行时间为1/e以及输入规模的多项式)')
        print('一个指数时间的准确算法')
        print('  假设对S的每个子集S\',都计算出S‘中所有元素的和.接着,在所有其元素和不超过t的子集中,选择其和最接近t的那个子集.',
            '显然,这一算法将返回最优解.但它可能需要指数级的时间.为了实现这个算法,可以采用一种迭代过程:在第i轮迭代中,计算{x1,x2,...,xi}的所有子集的元素和,',
            '计算的基础是{x1,x2,...,xi-1}的所有子集的和.在此计算过程中,一旦某个特定的子集S\'的和超过了t,就没有必要再对它进行处理了,因为S\'的超集都不会成为最优解')
        print('  过程EXACT-SUBSET-SUM的输入为一个集合S={x1,x2,...,xn}和一个目标值t;整个过程以迭代的方式计算列表Li,其中列出了{x1,x2,...,xi}的所有子集的和,',
            '这些和值都不超过目标值t.接着,它返回Ln中的最大值')
        print('如果L是一个由正整数所构成的表,x是一个正整数,用L+x来表示通过对L中每个元素增加x而导出的整数列表.例如,如果L=<1,2,3,5,9>,则L+2=<3,4,5,7,11>')
        print('一个完全多项式时间近似方案')
        print('  对于子集和问题,可以导出一个完全多项式时间近似方案,在每个列表Li被创建后,对它进行“修整”.具体的思想是如果L中的两个值比较接近,',
            '那么,处于寻找近似解的目的,没有理由同时保存这两个数.更准确地说,采用一个修整参数d,满足0<d<1,按d来修整一个列表L意味着以这样一种方式从L中除尽可能多的元素,即如果L\'为修整L后的结果,',
            '则对从L中去除的每个元素y,都存在着一个仍在L\'中的,近似y的元素z,使得y/(1+d)<=z<=y')
        print('  例如d=0.1,L=<10,11,12,15,20,21,22,23,24,29>,可以修整L得L\'=<10,12,15,20,23,29>')
        print('定理35.8 APPROX-SUBSET-SUM是关于子集和问题的一个完全多项式时间近似方案')
        print('练习35.1-1 ')
        print('练习35.1-2 ')
        print('练习35.1-3 ')
        print('练习35.1-4 ')
        print('思考题35-1 ')
        print('思考题35-2 ')
        print('思考题35-3 ')
        print('思考题35-4 ')
        print('思考题35-5 ')
        # python src/chapter35/chapter35note.py
        # python3 src/chapter35/chapter35note.py

chapter35_1 = Chapter35_1()
chapter35_2 = Chapter35_2()
chapter35_3 = Chapter35_3()
chapter35_4 = Chapter35_4()
chapter35_5 = Chapter35_5()

def printchapter35note():
    """
    print chapter35 note.
    """
    print('Run main : single chapter thirty-five!')
    chapter35_1.note()
    chapter35_2.note()
    chapter35_3.note()
    chapter35_4.note()
    chapter35_5.note()

# python src/chapter35/chapter35note.py
# python3 src/chapter35/chapter35note.py

if __name__ == '__main__':  
    printchapter35note()
else:
    pass
