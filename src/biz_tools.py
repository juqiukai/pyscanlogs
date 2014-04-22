# coding=gbk
__author__ = 'qitai.hyt'

import time

'''
根据原始日志文件路径、是否以时间结尾标识符和连接符，获取新的日志文件路径
@param logPath 初始日志文件路径
@param is_end_date    是否以日期结尾
@param connectChar  连接符号
'''
def changeLogPath(logPath, is_end_date, connectChar):
    if not is_end_date:
        return logPath
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return logPath + connectChar + date