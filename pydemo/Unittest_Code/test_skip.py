import unittest

class skip_test(unittest.TestCase):

    @unittest.skip("没理由就不能跳过吗")
    def test_skip1(self):
        self.assertEqual(1, 2)
        print("1")

    @unittest.skipIf(1>2, "skip")
    def test_skip2(self):
        print("2")