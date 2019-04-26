#-*- coding:utf-8 -*-
# 导入单元测试
import unittest
# 导入selenium
from selenium import webdriver
# 导入休眠包
import time
# 导入显式休眠的包
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 声明类 () 代表继承
class LoginUserPwd(unittest.TestCase):


    # 在所有测试用例运行之前执行
    # 想使用必须加注解 @classmethod
    @classmethod
    def setUpClass(self):

        pass

    # 在每一条测试用例运行之前执行
    def setUp(self):

        # 定义driver
        # 自己定义的变量 driver
        self.driver = webdriver.Firefox()
        # 设置浏览器最大化
        self.driver.maximize_window()
        # 打开指定网页
        self.driver.get("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a2a8f5a41b6c4cb0aeeb1fbd3effd300")

        # 设置休眠
        # time.sleep(10)
        # 使用显示休眠
        self.about_me = (By.LINK_TEXT,"关于我们")
        # 显示休眠
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(self.about_me))
        pass

        def test1(self):
            u"""用户名为空,密码为空"""
            # 打开查找控件
            self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
            # 设置点击事件
            self.login_tab_r.click()

            # 查询用户名输入框 以及密码输入框 和登陆按钮
            # 用户名
            self.loginname = self.driver.find_element_by_id("loginname")
            # 密码
            self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
            # 登陆按钮a
            self.login_btn = self.driver.find_element_by_class_name("login-btn")

            # 打开浏览器
            # 输入用户名为空
            self.loginname.send_keys(" ")
            # 输入密码为空
            self.nloginpwd.send_keys(" ")
            # 点击登陆按钮
            self.login_btn.click()

            # 设置休眠方式
            # 使用显式休眠
            # 通过 by获取
            msg = (By.CLASS_NAME, "msg-error")
            # driver
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(msg))

            # 进行断言
            self.msg_error = self.driver.find_element_by_class_name("msg-error");

            # 获取内容
            message = self.msg_error.text;

            # 进行断言
            assert (message, "请输入账户和密码")
            pass

    def test2(self):
        u"""用户名为doubenzhi1,密码为12315151515515"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("doubenzhi1")
        self.nloginpwd.send_keys("12315151515515")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "请输入正确的账户密码")
        pass

    def test3(self):
        u"""用户名为doubenzhi1,密码为空"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("17538330192")
        self.nloginpwd.send_keys(" ")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "请输入密码")
        pass

    def test4(self):
        u"""用户名为空,密码为11111111111"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("")
        self.nloginpwd.send_keys("11111111")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "请输入账户名")
        pass

    def test5(self):
        u"""用户名为12345678910111213141516,密码为14785296333"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("123456789101112121212")
        self.nloginpwd.send_keys("15313603021")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "请输入账户名")
        pass

    def test6(self):
        u"""用户名为17538330192,密码为11111111111111111111"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("17538330192")
        self.nloginpwd.send_keys("11111111111111111111")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "账户名与密码不匹配，请重新输入")
        pass

    def test7(self):
        u"""用户名为doubenzhi1,密码为521wei.."""

        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.loginname = self.driver.find_element_by_id("loginname")
        self.nloginpwd = self.driver.find_element_by_id("nloginpwd")
        self.login_btn = self.driver.find_element_by_class_name("login-btn")
        self.loginname.send_keys("xuhao12345")
        self.nloginpwd.send_keys("hao.521.")
        self.login_btn.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "账户密码正确")
        pass

    def test8(self):
        """QQ登录"""
        weixin_icon = (By.CLASS_NAME, "QQ-icon")
        # 设置休眠
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(weixin_icon))

        # 查找元素
        self.weixin_icon_login = self.driver.find_element_by_class_name("QQ-icon")

        # 设置点击按钮
        self.weixin_icon_login.click()

        # 点击到微信登陆页面加载需要时间,所以我们需要显式休眠
        # 想设置显式休眠必须有一个元素出现来进行判断

        # 寻找元素
        title = (By.CLASS_NAME, "text_hide")
        # 设置休眠
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(title))

        # 进行断言
        assert self.driver.title, "QQ登录"

    pass

    def test9(self):
            # 查询 微信登陆按钮
            # 在查询元素之前,首先设置显式休眠
            weixin_icon = (By.CLASS_NAME, "weixin-icon")
            # 设置休眠
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(weixin_icon))

            # 查找元素
            self.weixin_icon_login = self.driver.find_element_by_class_name("weixin-icon")

            # 设置点击按钮
            self.weixin_icon_login.click()

            # 点击到微信登陆页面加载需要时间,所以我们需要显式休眠
            # 想设置显式休眠必须有一个元素出现来进行判断

            # 寻找元素
            title = (By.CLASS_NAME, "title")
            # 设置休眠
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(title))

            # 进行断言
            assert self.driver.title, "微信登录"

            pass

    def test10(self):
        """"忘记密码"""
        self.login_tab_r = self.driver.find_element_by_class_name("login-tab-r")
        self.login_tab_r.click()
        self.forget_pw_safe = self.driver.find_element_by_class_name("forget-pw-safe")
        self.forget_pw_safe.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "忘记密码")
        pass

    def test11(self):
        """"个人注册"""
        self.regist_link = self.driver.find_element_by_class_name("regist-link")
        self.regist_link.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "个人注册")
        pass

    def test12(self):
        """"联系我们"""
        self.contact_us = self.driver.find_element_by_link_text("联系我们")
        self.contact_us.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "联系我们")
        pass

    def test13(self):
        """"人才招聘"""
        self.talent_recruitment = self.driver.find_element_by_link_text("人才招聘")
        self.talent_recruitment.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "人才招聘")
        pass

    def test14(self):
        """"商家入驻"""
        self.Merchants_settled = self.driver.find_element_by_link_text("商家入驻")
        self.Merchants_settled.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "商家入驻")
        pass

    def test15(self):
        """"广告服务"""
        self.advertising_service = self.driver.find_element_by_link_text("广告服务")
        self.advertising_service.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "广告服务")
        pass

    def test16(self):
        """"手机京东"""
        self.Mobile_phone_jingdong = self.driver.find_element_by_link_text("手机京东")
        self.Mobile_phone_jingdong.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "手机京东")
        pass

    def test17(self):
        """友情链接"""
        self.blogroll = self.driver.find_element_by_link_text("友情链接")
        self.blogroll.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "友情链接")
        pass

    def test18(self):
        """销售联盟"""
        self.Sales_of_union = self.driver.find_element_by_link_text("销售联盟")
        self.Sales_of_union.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "销售联盟")
        pass

    def test19(self):
        """京东社区"""
        self.Jingdong_community = self.driver.find_element_by_link_text("京东社区")
        self.Jingdong_community.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "京东社区")
        pass

    def test20(self):
        """京东公益"""
        self.Jingdong_public_welfare = self.driver.find_element_by_link_text("京东公益")
        self.Jingdong_public_welfare.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "京东公益")
        pass

    def test21(self):
        """English Site"""
        self.English_Site = self.driver.find_element_by_link_text("English Site")
        self.English_Site.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "English Site")
        pass

    def test22(self):
        """关于我们"""
        self.About_Us = self.driver.find_element_by_link_text("关于我们")
        self.About_Us.click()
        msg = (By.CLASS_NAME, "msg-error")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "关于我们")
        pass

    def test23(self):
        """京东隐私"""
        self.privacy = self.driver.find_element_by_class_name("black")
        # 设置点击事件
        self.privacy.click()
        msg = (By.CLASS_NAME, "msg-error")

        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "京东隐私")
        pass

    def test24(self):
        """登录访问"""
        self.q_link = self.driver.find_element_by_class_name("q-link")
        self.q_link.click()
        msg = (By.CLASS_NAME, "msg-error")

        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(msg))
        self.msg_error = self.driver.find_element_by_class_name("msg-error")
        message = self.msg_error.text
        assert (message, "登录页面")
        pass



    # 测试用例在Python里面是以test开头的
    # 测试用例的名字一定要见名知意,至少一条
    # 单元测试里面必须包含测试用例
    def testLoginUserPwd(self):

             pass

    # 每一条测试用例执行之后执行
    def tearDown(self):

        # 关闭浏览器
        self.driver.quit()


        pass

    # 所有测试用例执行之后执行
    # 想使用必须加注解 @classmethod
    @classmethod
    def tearDownClass(self):

        pass