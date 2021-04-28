# 703. 数据流中的第 K 大元素

## 题目

设计一个找到数据流中第` k `大元素的类（class）。注意是排序后的第` k `大元素，不是第` k `个不同的元素。

请实现 `KthLargest `类：

* `KthLargest(int k, int[] nums) `使用整数` k `和整数流 `nums `初始化对象。
* `int add(int val)` 将 `val `插入数据流` nums` 后，返回当前数据流中第 `k `大的元素。

## 示例

**示例 1：**

> 输入：
> ["KthLargest", "add", "add", "add", "add", "add"]
> [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
> 输出：
> [null, 4, 5, 5, 8, 8]
>
> 解释：
> KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
> kthLargest.add(3);   // return 4
> kthLargest.add(5);   // return 5
> kthLargest.add(10);  // return 5
> kthLargest.add(9);   // return 8
> kthLargest.add(4);   // return 8

## 提示

* `1 <= k <= 10^4`
* `0 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `-10^4 <= val <= 10^4`
* 最多调用 `add` 方法 `10^4` 次
* 题目数据保证，在查找第 `k` 大元素时，数组中至少有 `k` 个元素

## 解题思路

经典题，第k大元素则维护一个大小为k的小顶堆，堆顶的元素即为所求结果。

插入时，若堆的大小小于k，则直接插入。否则，只有val的值大于或等于堆顶时，才删除堆顶并插入val。

时间复杂度为O(nlogk)，空间复杂度为O(k)。

## 性能

执行用时：84 ms, 在所有 Python3 提交中击败了91.19%的用户

内存消耗：18.5 MB, 在所有 Python3 提交中击败了67.55%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。