# 543. 二叉树的直径

## 题目

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

**注意：**两结点之间的路径长度是以它们之间边的数目表示。

**示例1：**

> 给定二叉树
>
>              1
>             / \
>            2   3
>           / \     
>          4   5    
>返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
> 

## 解题思路

以某一个节点为最高顶点的路径，其最大长度为左子树的深度加右子树的深度。递归的过程中，维护一个最大路径长度即可。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：44 ms, 在所有 Python3 提交中击败了85.67%的用户

内存消耗：16.5 MB, 在所有 Python3 提交中击败了96.63%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。