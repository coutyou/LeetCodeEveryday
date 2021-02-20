# 144. 二叉树的前序遍历

## 题目

给定一个二叉树的根节点 `root` ，返回它的 **前序** 遍历。

## 示例

**示例 1：**

> 输入：root = [1,null,2,3]
> 输出：[1,2,3]

**示例 2：**

> 输入：root = []
> 输出：[]

**示例 3：**

> 输入：root = [1]
> 输出：[1]

**示例 4：**

> 输入：root = [1,2]
> 输出：[1,2]

**示例 5：**

> 输入：root = [1,null,2]
> 输出：[1,2]

## 提示

* 树中节点数目在范围 `[0, 100]` 内
* `-100 <= Node.val <= 100`

## 进阶

递归算法很简单，你可以通过迭代算法完成吗？

## 解题思路

递归算法比较简单，而迭代算法可以通过用栈模拟来完成。

思路与中序遍历类似，区别在于将节点的值添加到结果的顺序——中序遍历是在回溯时，切换到右子树之前。而前序遍历则是在向左延伸，入栈时。

时间复杂度为O(n)，空间复杂度为O(n)。

与中序遍历相同，存在**Morris**算法，能将空间复杂度降到O(1)。其核心思想是利用树的大量空闲指针，实现空间开销的极限缩减。详见[https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/)

## 性能

执行用时：32 ms, 在所有 Python3 提交中击败了94.24%的用户

内存消耗：15 MB, 在所有 Python3 提交中击败了5.15%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。