# 1003. 检查替换后的词是否有效

## 题目

给你一个字符串` s `，请你判断它是否**有效**。
字符串` s `**有效** 需要满足：假设开始有一个空字符串` t = "" `，你可以执行**任意次**下述操作将` t `**转换**为` s `：

* 将字符串` "abc" `插入到` t `中的任意位置。形式上，`t `变为` tleft + "abc" + tright`，其中` t == tleft + tright `。注意，`tleft `和` tright `可能为**空**。

如果字符串 `s`有效，则返回 `true`；否则，返回`false`。

## 示例

**示例 1：**

> 输入：s = "aabcbc"
> 输出：true
> 解释：
> "" -> "abc" -> "aabcbc"
> 因此，"aabcbc" 有效。

**示例 2：**

> 输入：s = "abcabcababcc"
> 输出：true
> 解释：
> "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
> 因此，"abcabcababcc" 有效。

**示例 3：**

> 输入：s = "abccba"
> 输出：false
> 解释：执行操作无法得到 "abccba" 。

**示例 4：**

> 输入：s = "cababc"
> 输出：false
> 解释：执行操作无法得到 "cababc" 。

## 提示

* `1 <= s.length <= 2 * 10000`
* `s` 由字母 `'a'`、`'b'` 和 `'c'` 组成

## 解题思路

类似泡泡龙，遇到a则入栈，b则检查前面是否有a，然后入栈，c则检查前面是否有a、b，然后出栈。最后检查栈是否为空。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：56 ms, 在所有 Python3 提交中击败了69.29%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.02%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。