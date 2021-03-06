# 144. 二叉树的前序遍历

## 题目

给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

**示例1：**

> 输入：root = [1,null,2,3]
> 输出：[1,2,3]

**示例2：**

> 输入：root = []
> 输出：[]

**示例3：**

> 输入：root = [1]
> 输出：[1]

**示例4：**

> 输入：root = [1,2]
> 输出：[1,2]

**示例5：**

> 输入：root = [1,null,2]
> 输出：[1,2]

## 进阶

递归算法很简单，你可以通过迭代算法完成吗？

## 解题思路

递归很简单，迭代的方法则需要通过维护一个栈，记录经过的节点，并在弹出时通过该节点切换到其右子树。

时间复杂度为O(n)，空间复杂度为O(n)。

## 提示

* 树中节点数目在范围 `[0, 100]` 内
* `-100 <= Node.val <= 100`

## 性能

执行用时：32 ms, 在所有 Python3 提交中击败了92.39%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了33.81%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。