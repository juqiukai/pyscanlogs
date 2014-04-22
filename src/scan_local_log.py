# coding=gbk
__author__ = 'Administrator'

import os
import time
import biz_tools

log_path = 'D:/logs/all-error.log'
is_end_with_date = True
date_format = 'yyyy-MM-dd'
connect_char = '`'


#根据开始行索引位置读取日志文件
def readLogs(logPath, begin_line_index):
    line_size = 0
    if not os.path.isfile(logPath):
        return -1
    file = open(logPath, 'r', 100)
    lines = file.readlines()[begin_line_index:]
    for line in lines:
        print line, line_size+begin_line_index+1
        line_size += 1
    file.close()
    return begin_line_index+line_size

if __name__ == '__main__':
    begin_line_index = 0
    last_log_path = ''
    while 1:
        current_log_path = biz_tools.changeLogPath(log_path, is_end_with_date, connect_char)
        if is_end_with_date and begin_line_index != current_log_path:
            begin_line_index = 0
        begin_line_index = readLogs(current_log_path, begin_line_index)
        if -1 == begin_line_index:
            print "日志文件不存在[logPath:"+current_log_path+"]"
            break
        time.sleep(3)
