# Auto_Sqlmap_scanner
 利用SQLmapapi做的批量注入点检测，多线程测试

# How To Use
 把注入点放进target.txt里面

 打开sqlmapapi`python3 sqlmapapi.py -s`

 然后运行main.py即可

# Notice
 请勿用于非法用途

 存了日志，将在最近几天继续优化

 taskid.txt作为容灾备份使用（程序意外退出）
 
# In Case
 以防万一，添加容灾备份，如果程序异常中断，可利用`in_case.py`进行救灾（对已经添加的任务取回结果）