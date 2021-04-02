# 剑指 Offer 59 - II. 队列的最大值

## 题目

请定义一个队列并实现函数 `max_value` 得到队列里的最大值，要求函数`max_value`、`push_back `和 `pop_front `的**均摊**时间复杂度都是O(1)。

若队列为空，`pop_front `和 `max_value` 需要返回 -1

## 示例

**示例 1：**

> 输入: 
> ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
> [[],[1],[2],[],[],[]]
> 输出: [null,null,null,2,1,2]

**示例 2：**

> 输入: 
> ["MaxQueue","pop_front","max_value"]
> [[],[],[]]
> 输出: [null,-1,-1]

## 提示

* `1 <= push_back,pop_front,max_value的总操作数 <= 10000`
* `1 <= value <= 10^5`

## 解题思路

一个元素加入队列后，队列的最大值与其前面比它小的值都没关系，可以忽略，所以可以维护一个单调不增栈。因为队列弹出时，单调栈也需要判断是否弹出栈底，所以单调栈同时也应该是双端队列。

均摊时间复杂度为O(1)，空间复杂度为O(n)。

## 性能

执行用时：248 ms, 在所有 Python3 提交中击败了46.24%的用户

内存消耗：18.6 MB, 在所有 Python3 提交中击败了10.43%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。