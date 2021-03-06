# 331. 验证二叉树的前序序列化

## 题目

序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 `#`。

```
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
```

例如，上面的二叉树可以被序列化为字符串` "9,3,4,#,#,1,#,#,2,#,6,#,#"`，其中` # `代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示` null `指针的` '#' `。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如` "1,,3" `。

## 示例

**示例 1：**

> 输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
> 输出: true

**示例 2：**

> 输入: "1,#"
> 输出: false

**示例 3：**

> 输入: "9,#,#,1"
> 输出: false

## 解题思路

题目中其实已经提示了，不需要对二叉树进行重构，也就是说，最后的结果与各个节点的值具体是多少无关，只与节点的种类（数字or#）和节点的顺序有关。

那么什么样的数据是错误的呢，一种是#节点是数字节点的父节点，另一种是数字节点缺少#节点的子节点。

我起初想找到各个节点的父节点进行判断，但是单从先序遍历的信息来说是不够的，如前3个是1，2，#，你不能判断#的父节点是1还是2。所以一直理不清头绪，后来看了官方的解析才知道，可以通过槽进行判断——一个数字节点消耗1个槽，同时创造2个槽，一个#节点消耗1个槽，不创造槽。只需要遍历这些节点，判断遍历过程中槽是否缺少，以及最后槽是否刚好用完即可。这个方法的合理性依赖于先序遍历的特性——中间的节点先遍历，这与树的结构是类似的。

时间复杂度为O(n)，空间复杂度为O(1)。

## 性能

执行用时：36 ms, 在所有 Python3 提交中击败了94.75%的用户

内存消耗：14.7 MB, 在所有 Python3 提交中击败了79.94%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。