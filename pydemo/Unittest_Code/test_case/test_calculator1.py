from calculator import Calculator
import unittest

class simple_test(unittest.TestCase):

    # def setUp(self):
    #     print("start")

    def test_div(self):
        print("div")
        c = Calculator(9, 3)
        resule = c.div()
        self.assertEqual(resule, 3)

    def test_mul(self):
        print("mul")
        c = Calculator(4, 4)
        resule = c.mul()
        self.assertEqual(resule, 16)

    def test_aa(self):
        print("aa")
        a = "123"
        b = "12"
        self.assertIsNot(a, b)

    # def tearDown(self):
    #     print("end")

def suite():
    # suite = unittest.TestSuite()
    # suite.addTest(simple_test("test_add"))
    # suite.addTest(simple_test("test_sub"))
    # suite.addTests([simple_test('test_add'), simple_test('test_sub')])
    
    # 根据文件名批量创建测试套件
    suite = unittest.makeSuite(simple_test, 'test_aa')
    return suite

if __name__ == '__main__':
    unittest.main()

    # 将suite进行封装成suite()
    # suit = unittest.TestSuite()
    # suit.addTest(simple_test("test_div"))
    # suit.addTest(simple_test("test_mul"))

    # runner = unittest.TextTestRunner()
    # runner.run(suite())