# coding=gbk
__author__ = 'qitai.hyt'

import time

'''
����ԭʼ��־�ļ�·�����Ƿ���ʱ���β��ʶ�������ӷ�����ȡ�µ���־�ļ�·��
@param logPath ��ʼ��־�ļ�·��
@param is_end_date    �Ƿ������ڽ�β
@param connectChar  ���ӷ���
'''
def changeLogPath(logPath, is_end_date, connectChar):
    if not is_end_date:
        return logPath
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return logPath + connectChar + date