# 1190. 反转每对括号间的子串

## 题目

给出一个字符串 `s`（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中**不应**包含任何括号。

## 示例

**示例 1：**

> 输入：s = "(abcd)"
> 输出："dcba"

**示例 2：**

> 输入：s = "(u(love)i)"
> 输出："iloveu"

**示例 3：**

> 输入：s = "(ed(et(oc))el)"
> 输出："leetcode"

**示例 4：**

> 输入：s = "a(bcdefghijkl(mno)p)q"
> 输出："apmnolkjihgfedcbq"

## 提示

* `0 <= s.length <= 2000`
* `s` 中只有小写英文字母和括号
* 我们确保所有括号都是成对出现的

## 解题思路

传统艺能，用栈的结构与括号结构对应。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：36 ms, 在所有 Python3 提交中击败了84.68%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.53%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。