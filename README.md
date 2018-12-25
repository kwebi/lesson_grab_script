# 北京交通大学自动化选课/抢课程序

## 如何运行

1. 安装Python
2. 需要FireFox浏览器，谁让我是FireFox粉呢, 你也可以替换为其他的
3. 安装selenium库, `pip install selenium`
4. `python robbing_class.py`

## 配置文件`config.json`

1. lesson_num为课程号/课程名称, 建议写课程号，精确度高一些
2. user_id 为学号
3. user_passwd 为mis系统密码
4. lesson_serial 为课程序列号，即同一课程号中每个课程的序号，可以为空, 则全选

## 目前提交时需要手动输入验证码

## 协议

禁止利用此代码于商业用途, 在此基础上还需要遵从GPL3.0协议