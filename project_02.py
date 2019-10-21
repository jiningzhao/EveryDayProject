'''
脚本功能：unittest单元测试
测试脚本：project/module.py
开发人员：赵吉宁
开发时间：2019-7-26 星期五
'''
import unittest
from project.module import Calculator

class ModuleTest(unittest.TestCase):

    #初始化函数
    def setUp(self):
        self.cal=Calculator(8,4)

    #善后函数
    def tearDown(self):
        pass

    def test_add(self):
        result=self.cal.add()
        self.assertEqual(12,result)

    def test_sub(self):
        result=self.cal.sub()
        self.assertEqual(4,result)

    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(32,result)

    def test_div(self):
        result=self.cal.div()
        self.assertEqual(2,result)

if __name__ == "__main__":
    #unittest.main()
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)