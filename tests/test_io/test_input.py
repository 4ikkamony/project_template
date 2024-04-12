import unittest
from app.io import input, output


# test read_file_pandas and read_file_defaul
class TestReadFileDefault(unittest.TestCase):
    def test_read_file_default_invalid_path_FileNotFoundError(self):
        file_path = 'invalid'
        expected = None
        actual = input.read_file_default(file_path)
        self.assertEqual(actual, expected)

    def test_read_file_default_one_line_success(self):
        expected = "Just a line of text"

        file_path = "D:\\wrkspc\\project_template\\data\\one_line_test.txt"
        output.write_file_default(expected, file_path)

        actual = input.read_file_default(file_path)

        self.assertEqual(actual, expected)

    def test_read_file_default_multi_line_success(self):
        expected = "multiple\nlines\nof\ntext"

        file_path = "D:\\wrkspc\\project_template\\data\\multi_line_test.txt"
        output.write_file_default(expected, file_path)

        actual = input.read_file_default(file_path)

        self.assertEqual(actual, expected)
