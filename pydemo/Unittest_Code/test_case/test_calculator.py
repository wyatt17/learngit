from calculator import Calculator
import unittest

class simple_test(unittest.TestCase):

    # def setUp(self):
    #     print("start")

    def test_add(self):
        print("add")
        c = Calculator(3, 5)   # 实例化
        result = c.add()
        assert result == 8
        
    def test_sub(self):
        print("sub")
        c = Calculator(2, 1)
        result = c.sub()
        self.assertEqual(result, 1, msg="有错")

    # def tearDown(self):
    #     print("end")

def suite():
    # 方法1
    # suite = unittest.TestSuite()
    # suite.addTest(simple_test("test_add"))
    # suite.addTest(simple_test("test_sub"))

    # 方法2
    # suite.addTests([simple_test('test_add'), simple_test('test_sub')])
    
    # 方法3
    # 根据文件名批量创建测试套件
    suite = unittest.makeSuite(simple_test, 'test')
    return suite 

if __name__ == '__main__':
    # unittest.main()

    # 将suite进行封装成suite()
    # suit = unittest.TestSuite()
    # suit.addTest(simple_test("test_add"))
    # suit.addTest(simple_test("test_sub"))

    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    # suites = unittest.TestLoader().discover('./test_case', pattern = 'test_*.py')
    unittest.TextTestRunner().run(suite())
