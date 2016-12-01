#!/usr/bin/env python
#coding:utf8

'''
    安装程序

    执行本脚本，会在 python 搜索路径中添加一个路径文件(.pth)，此文件内容为本项目的路径，实现导入功能
    标准库中的 site 可以显示此文件应该放的位置，site.getsitepackages() 可以查看
'''

import os
import sys
import site

projectDir = os.path.dirname(os.path.abspath(__file__))
projectName = os.path.split(os.path.basename(projectDir))[1]

fileName = '%s.pth' % projectName

for _path in site.getsitepackages():
    if _path.endswith('site-packages'):
        _confirm = raw_input("输入 Y/y 确认在此目录[%s]下创添加路径文件[%s]: "% (_path, fileName))
        if _confirm == 'y' or _confirm == "Y":
            with open('%s/%s' %(_path, fileName), 'w') as f:
                f.write(projectDir)
            print "文件[%s/%s]写入成功，请做导入测试。 "% (_path, fileName)
            break
        else:
            print '本次操作取消...'

print '执行完成...'
