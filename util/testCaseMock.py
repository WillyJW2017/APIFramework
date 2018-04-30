import unittest
import json
from mock import mock
from util.requestClass import RunMain
import HTMLTestRunner
from util.mockMethod import mock_test

class testMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        datadict = {
            'username': 'HelloWorld--Mock',
            'password': 'Welcome--Mock'
        }

        # mock_data = mock.Mock(return_value=datadict)
        # self.run.run_main = mock_data
        # res = self.run.run_main(url, 'POST', datadict)

        res = mock_test(self.run.run_main, url, 'POST', datadict, datadict)

        print(type(res))
        print(res)


    def test_02(self):
        print('This is the 02 test case')

    @unittest.skip('skip this test case no reason')
    def test_03(self):
        print('This is the 03 test case')


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

