# 94. 二叉树的中序遍历

## 题目

给定一个二叉树的根节点 `root` ，返回它的 **中序** 遍历。

## 示例

**示例 1：**

> 输入：root = [1,null,2,3]
> 输出：[1,3,2]

**示例 2：**

> 输入：root = []
> 输出：[]

**示例 3：**

> 输入：root = [1]
> 输出：[1]

**示例 4：**

> 输入：root = [1,2]
> 输出：[2,1]

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

对于当前节点，先一直往左扩展，直到最左，并将沿途的节点入栈。将最左节点的值加入结果中，再将指针指向最左节点的右节点。重复上述过程直到栈为空且指针为空。

时间复杂度为O(n)，空间复杂度为O(n)。

**Morris 遍历算法**可以将空间复杂度降为O(1)，其思路为找到当前节点在中序遍历结果中的前一个节点，即当前节点的左子树最右边的节点，并使该节点的右子树指针指向当前节点，这样在遍历完左子树后就可以通过该指针回到当前节点，而无需用栈来回溯。

具体代码详见[https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/)

## 性能

执行用时：32 ms, 在所有 Python3 提交中击败了93.73%的用户

内存消耗：14.8 MB, 在所有 Python3 提交中击败了27.49%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。