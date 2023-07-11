# douyin_auto-reply
依赖:```selenium==3.0.0```,浏览器chome+对应版本的chomedriver
# 使用selenium模拟人工逐条点击回复，回复list中预制好的内容；
- 当前代码只能回复depth=1的内容。
- 利用css 元素class定位回复按钮的位置，点击并输入回复内容，发送。
- 如果当前页面遍历完毕，会触发向下滑动的指令，更新页面中的元素数量。继续回复新增的可评论的评论。
- 本程序完全在cpu上运行。由于要避开抖音人工检查，时长间隔设置较长平均一条回复20s。
- 一旦运行，即全自动。不需要再更改，但是list中回复的内容也不会更新。
- 最大回复条数为10000;
![image](https://github.com/lizeyujack/douyin_auto-reply/assets/53364734/31914440-f85c-4b5a-91d2-e0337b44fea5)、
运行效果：https://www.bilibili.com/video/BV1JM4y1x7s1/

