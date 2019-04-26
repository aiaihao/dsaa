#-*- coding:utf-8 -*-
import  unittest
from  login import login
import  HTMLTestRunner
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

suit= unittest.TestSuite()

suit.addTest(unittest.makeSuite(login.LoginUserPwd))
file=os.getcwd()+"/login.html"
filename=open(file,"wb+")
runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title=u"许浩自动化测试报告",description=u"许浩的测试详情")
runner.run(suit)


