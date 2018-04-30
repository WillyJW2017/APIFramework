import unittest
import json
from util.requestClass import RunMain
import HTMLTestRunner

class testMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        # print('Test--->Setup')
    # def tearDown(self):
    #     print('Test--->tearDown')
    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        datadict = {
            'username': 'HelloWorldXXX',
            'password': 'WelcomeXXX'
        }

        res = self.run.run_main(url, 'POST', datadict)
        res = json.loads(res)
        print(type(res))
        print(res)
        # print('This is the 01 test case')

    def test_02(self):
        print('This is the 02 test case')
    def test_03(self):
        print('This is the 03 test case')
    # @classmethod
    # def setUpClass(cls):
    #     print('Test--->Start')
    # @classmethod
    # def tearDownClass(cls):
    #     print('Test--->End')


if __name__ == '__main__':
    # unittest.main()
    filepath = '../report/hreport.html'
    fp = open(filepath, 'wb')

    suite = unittest.TestSuite()
    suite.addTest(testMethod('test_01'))
    suite.addTest(testMethod('test_02'))
    suite.addTest(testMethod('test_03'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='This is the report title', description= 'This is the report description')
    runner.run(suite)
    fp.close()
    # unittest.TextTestRunner.run(suite)

