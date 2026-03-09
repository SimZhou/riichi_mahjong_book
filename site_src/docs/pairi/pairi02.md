# 有效牌与枚数

麻将本质上是在不断重复一件事：

**从手里找一张相对最没用的牌打掉。**

那“有没有用”该怎么衡量？最基础的指标，就是`有效牌的枚数`。

## 枚数越多，和牌概率越高

先看一个最直观的例子：

<img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man2.gif" width="24" height="34" /><img src="../hai/man3.gif" width="24" height="34" /><img src="../hai/man3.gif" width="24" height="34" /><img src="../hai/man3.gif" width="24" height="34" /><img src="../hai/man4.gif" width="24" height="34" /><img src="../hai/pin7.gif" width="24" height="34" /><img src="../hai/pin7.gif" width="24" height="34" /><img src="../hai/pin7.gif" width="24" height="34" /><img src="../hai/sou5.gif" width="24" height="34" /><img src="../hai/sou5.gif" width="24" height="34" /><img src="../hai/sou7.gif" width="24" height="34" /><img src="../hai/sou8.gif" width="24" height="34" /><img src="../hai/sou9.gif" width="24" height="34" />

这手里，除非 <img src="../hai/man3.gif" width="24" height="34" /> 极端危险，否则标准切法就是切一张 <img src="../hai/man3.gif" width="24" height="34" />。

原因很简单。比较两种待型：

1. 保留 `12334` 变成待 <img src="../hai/man2.gif" width="24" height="34" />、<img src="../hai/man5.gif" width="24" height="34" />
2. 保留 `12333` 变成待 <img src="../hai/man3.gif" width="24" height="34" />、<img src="../hai/sou5.gif" width="24" height="34" />

前者理想枚数是 `7`，后者理想枚数只有 `3`。

当然，牌山里实际剩几枚你不可能完全知道，但实战判断只能先从“理想剩余枚数”出发。也就是说：

1. 待牌种类和总枚数更多
2. 就意味着平均意义上更容易和
3. 长期看也就更赚

原页这里讲得很直白：你当然可能刚好遇到 `2m / 5m` 一张都不剩的极端情况，但你并没有超能力，不可能每次都知道真实山况。所以正常牌理判断，必须先以“理想枚数”作为比较基准。

所以“枚数越多越有利”不是口号，而是牌效率的底层原则。

原页甚至把这一步写成了完整逻辑链：

1. 待牌枚数更多
2. 就代表和牌概率更高
3. 长期就代表更常赚到分

麻将比的不是灵感，而是这种损益判断是否更稳定。

## 不听牌时，也一样靠枚数比较

很多人只会在听牌时比待牌，到了两向听、一向听阶段就开始凭感觉。

其实这时更该数枚数。

原页的那张图很关键：

<img src="../images/004.gif" width="229" height="227" />

意思是：

1. 两向听时，先争取更快进入一向听
2. 一向听时，先争取更快进入听牌
3. 不必一上来就幻想“最终哪张牌和”

因此最常用的数法，就是：

**比较能让当前向听数下降的牌有多少枚。**

原页这里等于是在提醒：离和牌还远的时候，不要直接去幻想最终哪张能和。先比较“谁能更快把你送到下一阶段”，这是更现实的算法。

## 什么叫受入枚数

例如下面这手：

<img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man2.gif" width="24" height="34" /><img src="../hai/man6.gif" width="24" height="34" /><img src="../hai/man8.gif" width="24" height="34" /><img src="../hai/pin4.gif" width="24" height="34" /><img src="../hai/pin4.gif" width="24" height="34" /><img src="../hai/pin6.gif" width="24" height="34" /><img src="../hai/sou1.gif" width="24" height="34" /><img src="../hai/sou2.gif" width="24" height="34" /><img src="../hai/sou3.gif" width="24" height="34" /><img src="../hai/sou3.gif" width="24" height="34" /><img src="../hai/sou4.gif" width="24" height="34" />

它是两向听。若要进入一向听，能帮你前进一步的牌有：

<img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man3.gif" width="24" height="34" /><img src="../hai/man7.gif" width="24" height="34" /><img src="../hai/pin4.gif" width="24" height="34" /><img src="../hai/pin5.gif" width="24" height="34" /><img src="../hai/sou2.gif" width="24" height="34" /><img src="../hai/sou5.gif" width="24" height="34" />

合计 `7 种 23 枚`。

这就是受入枚数。

也就是：能让这手牌从两向听前进到一向听的所有牌种，以及它们的总枚数。

## 枚数多的形，客观上更好

再看一个几乎相同、但结构更好的版本：

<img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man1.gif" width="24" height="34" /><img src="../hai/man2.gif" width="24" height="34" /><img src="../hai/man6.gif" width="24" height="34" /><img src="../hai/man8.gif" width="24" height="34" /><img src="../hai/pin4.gif" width="24" height="34" /><img src="../hai/pin4.gif" width="24" height="34" /><img src="../hai/pin6.gif" width="24" height="34" /><img src="../hai/sou2.gif" width="24" height="34" /><img src="../hai/sou3.gif" width="24" height="34" /><img src="../hai/sou3.gif" width="24" height="34" /><img src="../hai/sou4.gif" width="24" height="34" /><img src="../hai/sou4.gif" width="24" height="34" />

这手因为七对子路线也成立，原页给出的受入可以到 `13 种 35 枚`。

所以即便只是看上去“差不多”的两手牌，客观速度也可能差很多。数受入的意义就在这里：它能把模糊感觉变成可以比较的量。

原页这里的重点不是让你背这道题，而是告诉你：两手看上去只差一点点的牌，客观受入却可能差出一大截。只靠直觉很容易误判，数枚数才能把差别看实。

## 有效牌不只有“降向听”的那一种

继续看前面的例子，如果再摸进：

<img src="../hai/sou4.gif" width="24" height="34" />

向听数虽然不一定立刻下降，但下一步的受入会变宽。这种牌也属于有效牌。

因此，有效牌可以分成两类：

1. `A`：直接让向听数下降的牌，也就是受入
2. `B`：虽然不降向听，但会让 `A` 变多的牌，也就是好形变化

原页强调得很对：

**A 的价值高于 B。**

因为 `A` 代表你现在就能离和牌更近一步，而 `B` 只是让你“下一步可能更好”。这两者不能混为一谈。

## 枚数相同的时候，再比好形变化

有时两个选择当前受入一样，这时才轮到比较好形变化。

例如原页最后那手待牌选择：

1. 当前两种取法都是 `4 枚`
2. 但其中一种后续有三面变化
3. 另一种后续改善明显更少

这时当然要选后续变化更强的一边。

原页这题的结论就是：当前两边都是 `4` 枚时，取后续能长成三面变化的那一边，也就是继续保留双碰取法。

但顺序不能颠倒。基础牌效率永远先看：

1. 当前受入谁更大
2. 若相同，再看好形变化

原页最后专门提醒了一件很容易搞错的事：

1. 有些人会把 `A` 和 `B` 直接相加
2. 然后用 `受入 + 好形变化` 去比较两手牌

这通常是不对的。因为“立刻前进一步”和“以后可能变好”不是同等价值。

所以牌理的基本顺序必须固定：

**先比受入，再比好形变化。**

## 这一页的结论

1. “枚数越多越有利”是牌效率最基础的原则
2. 听牌阶段比待牌枚数，不听牌阶段比受入枚数
3. 受入就是能让当前向听数下降的牌
4. 有效牌还包括会扩大受入的好形变化
5. 但比较顺序必须是：`先看受入，再看好形变化`

---

原始日文页：<http://beginners.biz/pairi/pairi02.html>

<!-- PAGE NAV START -->
<div class="page-nav" markdown="0">
  <a class="page-nav__link page-nav__link--prev" href="pairi01.html">上一节：按牌理打牌</a>
  <a class="page-nav__link page-nav__link--next" href="pairi03.html">下一节：浮牌理论</a>
</div>
<!-- PAGE NAV END -->
