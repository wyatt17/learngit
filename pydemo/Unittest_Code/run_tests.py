import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner

test_dir = './test_case'
# 1.discover()方法会自动根据测试用例目录test_dir查找测试用例文件test_*.py
# 2.添加到套件中，通过run()方法执行套件
suites = unittest.TestLoader().discover(test_dir, pattern = 'test_*.py')

now=time.strftime("%Y%m%d%H%M%S", time.localtime())  
filename=r'./report/'+now+r'result.html' # 根据时间生成文件名

#   定义测试报告存放路径，
#   wb  如果已存在这个文件则删除原来内容，重新编辑；不存在该文件则新建文件，
#   所以使用时间now生成文件名，可以将每一次的测试报告都保留下来
fp=open(filename, 'wb')  

if __name__  == '__main__':
    # 3.通过run()方法执行套件
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,title='报告标题',description='报告说明' )
    runner.run(suites)