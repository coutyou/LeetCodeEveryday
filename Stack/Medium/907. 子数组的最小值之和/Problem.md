# 907. 子数组的最小值之和

## 题目

给定一个整数数组` arr`，找到` min(b) `的总和，其中` b `的范围为` arr `的每个（连续）子数组。

由于答案可能很大，因此 返回答案模` 10^9 + 7 `。

## 示例

**示例 1：**

> 输入：arr = [3,1,2,4]
> 输出：17
> 解释：
> 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
> 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

**示例 2：**

> 输入：arr = [11,81,94,43,3]
> 输出：444

## 提示

* `1 <= arr.length <= 3 * 10^4`
* `1 <= arr[i] <= 3 * 10^4`

## 解题思路

看题目的时候没看到是连续的子数组，想了半天最后看了解析，[https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-zuo-you-liang-bian-di-yi-g-ww3n/](https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-zuo-you-liang-bian-di-yi-g-ww3n/)讲得挺好的。

时间复杂度为O(n)，空间复杂度为O(n)。

## 性能

执行用时：188 ms, 在所有 Python3 提交中击败了58.80%的用户

内存消耗：17.9 MB, 在所有 Python3 提交中击败了82.40%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。