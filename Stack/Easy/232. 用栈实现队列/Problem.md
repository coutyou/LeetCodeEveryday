# 232. 用栈实现队列

## 题目

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（`push`、`pop`、`peek`、`empty`）：

实现 `MyQueue` 类：

* `void push(int x)` 将元素 x 推到队列的末尾
* `int pop()` 从队列的开头移除并返回元素
* `int peek()` 返回队列开头的元素
* `boolean empty()` 如果队列为空，返回 true ；否则，返回 false

**注意：**

* 你只能使用标准的栈操作 —— 也就是只有 `push to top`, `peek/pop from top`, `size`, 和 `is empty` 操作是合法的。
* 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。


## 示例

**示例 1：**

> 输入：
> ["MyQueue", "push", "push", "peek", "pop", "empty"]
> [[], [1], [2], [], [], []]
> 输出：
> [null, null, null, 1, 1, false]
>
> 解释：
> MyQueue myQueue = new MyQueue();
> myQueue.push(1); // queue is: [1]
> myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
> myQueue.peek(); // return 1
> myQueue.pop(); // return 1, queue is [2]
> myQueue.empty(); // return false

## 提示

* 1 <= x <= 9
* 最多调用 100 次 `push`、`pop`、`peek` 和 `empty`
* 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）


## 进阶

你能否实现每个操作均摊时间复杂度为 `O(1)` 的队列？换句话说，执行 `n` 个操作的总时间复杂度为 `O(n)` ，即使其中一个操作可能花费较长时间。

## 解题思路

根据栈的性质，其可以进行类似竹筒倒豆子的操作。但是从一个栈倒入另一个栈时，其顺序肯定是相反的。

要用栈来实现队列的效果，`push`和`pop`要同时在O(1)的时间复杂度内实现是不可能的。

假设`push`时间复杂度为O(1)，那么每次将其插入栈1的最后即可。但`pop`的时候，因为该元素在栈底，所以需要类似竹筒倒豆子，将栈1的元素倒入栈2，再从栈2的栈顶弹出，这时再倒回去，时间复杂度为O(n)。`peek`为栈1的栈底元素，时间复杂度为O(1)。`empty`只需判断栈1是否为空，时间复杂度为O(1)。

反之，假设`pop`时间复杂度为O(1)，那么需要使其保持在栈2的栈顶，即保持栈2为满，栈1为空，这需要在每次`push`时，先从栈2倒入栈1，再从栈1倒入栈2，因此时间复杂度为O(n)。`top`为栈2栈顶的元素，时间复杂度为O(1)。`empty`只需判断栈2是否为空，时间复杂度为O(1)。

这两种方法其实并没有本质区别，只不过第二种方法里，`push`时就提前帮`pop`把栈顶元素移到前端了。

但是，其实还有可以优化的空间。我们发现第一种方法能很方便进行连续的`push`操作，而第二种方法能很方便进行连续的`pop`操作，那么能不能将两者进行结合呢？从上面可以知道，第一种方法需要保持栈1为满、栈2为空，第二种则需要保持栈2为满、栈1为空，在倒入另一个栈又倒回来的过程中，浪费了很多时间。那么能不能同时使用这两个栈呢？稍微思考一下就能发现，其实没有必要来回倒，因为栈2中的元素对应的是“队列”前端的元素，栈1则对应“队列”后端的元素，因此`push`和`pop`之间并不冲突，栈1负责`push`，栈2负责`pop`，当栈2为空时，再将栈1的元素倒入。

因此，`push`时间复杂度为O(1)，`pop`最坏情况下时间复杂度为O(n)，一般情况下为O(1)，均摊时间复杂度为O(1)，`peek`和`empty`时间复杂度为O(1)。空间复杂度为O(n)。

至于为什么1个队列就可以实现栈，而实现队列至少需要2个栈，我认为是因为栈只能操作1端，而队列可以操作2端。

## 性能

执行用时：36 ms, 在所有 Python3 提交中击败了79.69%的用户

内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.24%的用户

## 声明

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。