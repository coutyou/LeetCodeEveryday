# 783. 二叉搜索树节点最小距离

## 题目

给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

**示例1：**

> 输入：root = [4,2,6,1,3]
>    输出：1

**示例2：**

> 输入：root = [1,0,48,null,null,12,49]
> 输出：1

## 提示

* 树中节点数目在范围 `[2, 100]` 内
* `0 <= Node.val <= 10^5`
* 差值是一个正数，其数值等于两值之差的绝对值

## 解题思路

二叉搜索树中序遍历，与前一个值做差，更新最小距离和前一个值。

时间复杂度：O(n)。

空间复杂度：O(n) 。

## 性能

执行用时：36 ms, 在所有 Python3 提交中击败了59.55%的用户

内存消耗：15 MB, 在所有 Python3 提交中击败了41.80%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。