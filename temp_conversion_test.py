'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import io
from unittest import mock, TestCase

from temp_conversion import *


class TestTempConversion(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_100_to_celsius(self, mock_stdout):
        convert_100_to_celsius()
        
        self.assertEqual('37.77777777777778\nfloat\n', mock_stdout.getvalue())


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_0_to_celsius(self, mock_stdout):
        convert_0_to_celsius()
        
        self.assertEqual('-17.77777777777778\n', mock_stdout.getvalue())


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_34_2_to_celsius(self, mock_stdout):
        convert_34_2_to_celsius()
        
        self.assertEqual('1.2222222222222239\n', mock_stdout.getvalue())


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_5_to_fahrenheit(self, mock_stdout):
        convert_5_to_fahrenheit()
        
        self.assertEqual('41.0\n', mock_stdout.getvalue())


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hotter_temp(self, mock_stdout):
        hotter_temp()
        
        self.assertEqual('30.2 degrees celsius\n', mock_stdout.getvalue())