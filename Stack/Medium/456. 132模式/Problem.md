# 456. 132模式

## 题目

给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

**注意：** n 的值小于15000。

## 示例

**示例 1：**

> 输入: [1, 2, 3, 4]
> 
> 输出: False
> 
> 解释: 序列中不存在132模式的子序列。

**示例 2：**

> 输入: [3, 1, 4, 2]
> 
> 输出: True
> 
> 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

**示例 3：**

> 输入: [-1, 3, 2, 0]
>
> 输出: True
>
> 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
>

## 解题思路

对于任一节点，想找到以其为中间节点的132组合，那么左边的节点应该尽量小，所以可以维护一个最小值的列表。右边节点的值应该介于左节点和中间节点的值之间。那么有两种思路，一种是找到所有右边节点值中大于左节点值的最小值，然后与中间节点值对比。另一种是找到所有右边节点值中小于中间节点值的最大值，然后与左节点值进行对比。但是，注意到最小值列表从左到右是单调不增的，所以利用这个性质，并在从右向左遍历时，维护一个右边的单调不增栈，能很方便地找到大于左节点值的最小值。

[https://leetcode-cn.com/problems/132-pattern/solution/zhan-jie-fa-chao-xiang-xi-ti-jie-by-siyy/](https://leetcode-cn.com/problems/132-pattern/solution/zhan-jie-fa-chao-xiang-xi-ti-jie-by-siyy/)讲解得很好，可以参考。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：44 ms, 在所有 Python3 提交中击败了92.91%的用户

内存消耗：15.8 MB, 在所有 Python3 提交中击败了5.20%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。