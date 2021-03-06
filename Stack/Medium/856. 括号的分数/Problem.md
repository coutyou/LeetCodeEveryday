# 856. 括号的分数

## 题目

给定一个平衡括号字符串` S`，按下述规则计算该字符串的分数：

* ` () `得 1 分。
* ` AB `得` A + B `分，其中` A `和` B `是平衡括号字符串。
* ` (A) ` 得` 2 * A `分，其中` A `是平衡括号字符串。

## 示例

**示例 1：**

> 输入： "()"
> 输出： 1

**示例 2：**

> 输入： "(())"
> 输出： 2

**示例 3：**

> 输入： "()()"
> 输出： 2

**示例 4：**

> 输入： "(()(()))"
> 输出： 6

## 提示

* `S` 是平衡括号字符串，且只含有 `(` 和 `)` 。
* `2 <= S.length <= 50`

## 解题思路

又是一题利用栈与括号的层次对应关系进行解题的题目，不再赘述。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：24 ms, 在所有 Python3 提交中击败了100.00%的用户

内存消耗：14.8 MB, 在所有 Python3 提交中击败了65.44%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。