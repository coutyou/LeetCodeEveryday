# 844. 比较含退格的字符串

## 题目

给定` S `和` T `两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。` # `代表退格字符。

**注意：**如果对空文本输入退格字符，文本继续为空。


## 示例

**示例 1：**

> 输入：S = "ab#c", T = "ad#c"
> 输出：true
> 解释：S 和 T 都会变成 “ac”。

**示例 2：**

> 输入：S = "ab##", T = "c#d#"
> 输出：true
> 解释：S 和 T 都会变成 “”。

**示例 3：**

> 输入：S = "a##c", T = "#a#c"
> 输出：true
> 解释：S 和 T 都会变成 “c”。

**示例 4：**

> 输入：S = "a#c", T = "b"
> 输出：false
> 解释：S 会变成 “c”，但 T 仍然是 “b”。

## 提示

* `1 <= S.length <= 200`
* `1 <= T.length <= 200`
* `S` 和 `T` 只含有小写字母以及字符 `#`

## 进阶

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

## 解题思路

不考虑空间复杂度的情况下很简单，使用模拟法，用栈逐个处理S和T中的数据即可，最后比较结果。时间复杂度为O(n)，空间复杂度为O(n)。

但仔细思考可以发现，一个字符是否会被删掉，只取决于该字符后面的退格符，而与该字符前面的退格符无关。因此当我们逆序地遍历字符串，就可以立即确定当前字符是否会被删掉。

为了实现O(1) 的空间复杂度，需要用双指针法，分别逆序遍历S和T，一个个地找到未被#删除的字符。可以用一个变量cnt记录逆序时经过的#的个数，遇到非#字符则消耗1个，当cnt为0时，说明找到了一个未被#删除的字符。然后将S和T中找到的进行对比。时间复杂度为O(n)，空间复杂度为O(1)。

## 性能

执行用时：36 ms, 在所有 Python3 提交中击败了83.73%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了14.07%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。