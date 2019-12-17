# ZUCC_xk_ZhengFang 正方教务系统自动抢课助手

正方教务系统模拟登录，爬取信息，自动抓包发包抢课
*抢课需谨慎，记得看注意事项*

> 程序仅供交流学习，请勿用作非法用途

### 环境需求
1. python环境 ：Python3.5+
2. 程序依赖 :  requests  bs4 PIL
3. 当前windows、ubuntu、mac测试可用

### 使用步骤
1. git clone源码
2. 运行源码中的main.py文件
3. 第一次运行先选择设置账号密码(之后运行直接选开始抢课,之前的账号密码会保存在account.json文件中)


### 注意事项
1. 第一次运行计划内选课的时候需要先进行更新，将课程缓存入文件，否则无法抢计划内课程和大学英语拓展课
2. 注意正方教务系统中进行计划内选课时，如果已有该课程，再次提交同样课程不同时间段的选课申请，有可能会删除你的已选课程 ,抢课之前请再三确认你要抢的课(若课程被删了，我不负责哦)
3. 跨专业选课暂时还未开发完成，如有需要可以联系我，给你私人定制版
`tel:13588362431`