# 155. 最小栈

## 题目

设计一个支持 `push `，`pop `，`top` 操作，并能在常数时间内检索到最小元素的栈。

* push(x) —— 将元素 x 推入栈中。
* pop() —— 删除栈顶的元素。
* top() —— 获取栈顶元素。
* getMin() —— 检索栈中的最小元素。

## 示例

**示例 1：**

> 输入：
> ["MinStack","push","push","push","getMin","pop","top","getMin"]
> [[],[-2],[0],[-3],[],[],[],[]]
>
> 输出：
> [null,null,null,null,-3,null,0,-2]
>
> 解释：
> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.getMin();   --> 返回 -3.
> minStack.pop();
> minStack.top();      --> 返回 0.
> minStack.getMin();   --> 返回 -2.

## 提示

* `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用。

## 解题思路

本题较简单，除了储存数据需要一个栈之外，我们还需维护一个相同长度的最小值栈，用于记录数据栈对应位置及之前位置数据的最小值。

这是栈的特性决定的，最小值栈的出栈操作并不会影响到之前位置的数据的最小值性质。

空间复杂度为O(n)，`push`、`pop`、`top` 和 `getMin` 操作的时间复杂度均为O(1)。

## 性能

执行用时：60 ms, 在所有 Python3 提交中击败了94.17%的用户

内存消耗：18 MB, 在所有 Python3 提交中击败了15.99%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。