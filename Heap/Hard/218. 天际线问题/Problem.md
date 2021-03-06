# 218. 天际线问题

## 题目

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 **天际线** 。

每个建筑物的几何信息由数组` buildings `表示，其中三元组 `buildings[i] = [left_i, right_i, height_i]` 表示：

* `left_i `是第 `i `座建筑物左边缘的 `x` 坐标。
* `right_i `是第` i` 座建筑物右边缘的 `x` 坐标。
* `height_i` 是第` i `座建筑物的高度。

**天际线**应该表示为由 “关键点” 组成的列表，格式 `[[x1,y1],[x2,y2],...]` ，并按 **x 坐标** 进行 排序 。**关键点是水平线段的左端点**。列表中最后一个点是最右侧建筑物的终点，`y `坐标始终为 `0` ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

**注意**：输出天际线中不得有连续的相同高度的水平线。例如 `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：`[...[2 3], [4 5], [12 7], ...]`

## 示例

**示例 1：**

>       输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
>       输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
>       解释：
>       图 A 显示输入的所有建筑物的位置和高度，
>       图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。

**示例 2：**

>       输入：buildings = [[0,2,3],[2,5,3]]
>       输出：[[0,3],[5,0]]

## 提示

* `1 <= buildings.length <= 10^4`
* `0 <= left_i < right_i <= 2^31 - 1`
* `1 <= height_i <= 2^31 - 1`
* `buildings` 按 `left_i` 非递减排序

## 解题思路

因为天际线是所有高度的最大值，所以从左到右进行遍历时维护一个最大堆。

因为只有在关键点（建筑物的左右端点）时，天际线才可能会发生变化，所以先对所有关键点进行排序，再进行遍历。堆中的节点需要记录建筑物的高度，以及右端点，用于判断什么时候“过期”。对于高度是大顶堆，对于右端点是小顶堆，因此其中一个要取负数。

而如何处理堆中“过期”的节点，如果每次都要遍历清理掉所有”过期“节点，时间复杂度较高。可以只删除掉堆顶那些会影响此次循环的节点，即不断弹出，直到堆顶的节点未”过期“。然后把建筑物数组中的左端点等于当前关键点的建筑物入堆，因为建筑物数组已经按照左端点从小到大进行排序了，所以可以维护一个建筑物数组的下标，用于将节点入堆。

时间复杂度为O(nlogn)，空间复杂度为O(n)。

## 性能

执行用时：64 ms, 在所有 Python3 提交中击败了79.18%的用户

内存消耗：18.7 MB, 在所有 Python3 提交中击败了72.32%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。