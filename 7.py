import unittest
from hash import Greeter
from unittest.mock import Mock, patch
from datetime import datetime


# class MD5TestCase(unittest.TestCase):
#     @patch('hash.md5')
#     def test_some_test(self, mock_md5):
#         hash_md5('some str')
#         print(mock_md5.calls)
#         mock_md5.assert_called_with(
#             'some str'.encode()
#         )


# class StringTestCase(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'Foo')
#
#     @patch('hashlib.md5')
#     def test_profile(self, mock_md5):
#         mock_md5()
#         mock_md5.return_value = 'Some hash'
#         mock_md5.assert_called_with('some param')
#         mock_md5.calls()
#         profile = Mock(first_name='Ivan')
#         print(profile.first_name)
#         profile.balance.return_value = 15
#         profile.balance.side_effect = Exception('some error')
#         print(profile.balance())

class GreeterTestCase(unittest.TestCase):
    def test_greet(self):
        gr = Greeter()
        self.assertEqual(gr.greet('Ivan'), 'Hello Ivan')

    def test_greet_2(self):
        gr = Greeter()
        self.assertEqual(gr.greet(' Ivan '), 'Hello Ivan')

    def test_greet_3(self):
        gr = Greeter()
        self.assertEqual(gr.greet('ivan'), 'Hello Ivan')

    @patch('hash.datetime')
    def test_greet_4(self, mock_datetime):
        gr = Greeter()
        mock_datetime.now.return_result = datetime.strptime('2018-05-23 12:30', "%Y-%d-%m %I:%M")
        self.assertEqual(gr.greet('ivan'), 'Good evening Ivan')


