二分法的核心是:

    1. 确定左右区间, 可分为4种形式:
        a. [left, right]
        b. [left, right)
        c. (left, right]
        d. (left, right)
        不同的开闭区间设置将影响跳出while循环的判断(left<=right or left<right);
    2. 设置跳出循环的判断;
    3. 循环中左右边界移动的设置;

参考资料:

    1. 基础内容, [分享｜二分查找边界分析] (https://leetcode.cn/circle/discuss/O3hHVH/)
    2. [数组专场，二分查找，左右边界问题] (https://blog.csdn.net/qq_32727095/article/details/124016937)
