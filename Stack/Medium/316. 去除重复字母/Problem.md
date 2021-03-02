# 316. 去除重复字母

## 题目

给你一个字符串 `s` ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证**返回结果的字典序最小**（要求不能打乱其他字符的相对位置）。

**注意：**该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

## 示例

**示例 1：**

> 输入：s = "bcabc"
> 输出："abc"

**示例 2：**

> 输入：s = "cbacdcbc"
> 输出："acdb"

## 提示

* `1 <= s.length <= 10000`
* `s `由小写英文字母组成

## 解题思路

本题是一种较为经典的题型，可以在https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/中查看详细解析。

用单调栈来遍历，但是出栈时要考虑之后还有没有该字符，没有的话就不能出栈。并且如果遇到的元素在栈中出现过，就可以直接跳过。

时间复杂度为O(n)，空间复杂度为O(1)。

## 性能

执行用时：40 ms, 在所有 Python3 提交中击败了90.04%的用户

内存消耗：14.8 MB, 在所有 Python3 提交中击败了52.30%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。