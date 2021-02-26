# 173. 二叉搜索树迭代器

## 题目

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 `next()` 将返回二叉搜索树中的下一个最小的数。

## 示例

**示例 1：**

> BSTIterator iterator = new BSTIterator(root);
> iterator.next();    // 返回 3
> iterator.next();    // 返回 7
> iterator.hasNext(); // 返回 true
> iterator.next();    // 返回 9
> iterator.hasNext(); // 返回 true
> iterator.next();    // 返回 15
> iterator.hasNext(); // 返回 true
> iterator.next();    // 返回 20
> iterator.hasNext(); // 返回 false
>

## 提示

* `next()` 和 `hasNext()` 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
* 你可以假设 `next()` 调用总是有效的，也就是说，当调用 `next()` 时，BST 中至少存在一个下一个最小的数。

## 解题思路

一个直观的思路就是将中序遍历的结果先存在一个数组中，需要时再返回。`next()` 和 `hasNext()` 操作的时间复杂度是 O(1)，空间复杂度为O(n)。

但题目要求的是迭代器，因此并没有必要一次性将所有结果保存下来，而是可以惰性地取出，而这就不能使用较为简单的递归式中序遍历，而需要进行迭代式地中序遍历，好在这种遍历方法我们之前实现过，只需在此基础上稍微修改即可。`next()` 和 `hasNext()` 操作的时间复杂度是 O(1)，因为维护的栈不超过树的高度，因此空间复杂度为O(h)。

## 性能

执行用时：80 ms, 在所有 Python3 提交中击败了94.58%的用户

内存消耗：21.6 MB, 在所有 Python3 提交中击败了25.09%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。