import unittest
import project
import argparse
import sys
import io


class TestProject(unittest.TestCase):
    def write(self, arg):
            pass

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('excel', type=str, action='store',
                                 help='path to xlsx file', nargs=1)
        self.parser.add_argument('-c', '--create', action='store_true',
                                 help='flag if entered file is to add new table to database')
        self.parser.add_argument('-ai', '--add_index', action='store', type=int,
                                 help="adds index to the entered column by its number, if table and column exists",
                                 nargs=1)
        self.parser.add_argument('-upd', '--update', action='store_true',
                                 help="flag if entered file is to update the existing table")

    def test_empty_file(self):  # testing if we have have not entered path to data
        data = ["./test_data/test1.xlsx", "-c"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Table given is empty. Enter any data and try again.')

    def test_no_args(self):  # testing with no argument argparse systemexit error == 2
        # redirect error outputs of argparse lib to nowhere, they are catched, that's ok.
        sys.stderr = io.StringIO()
        data = []
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        sys.stderr = sys.__stderr__
        self.assertEqual(cm.exception.code, 2)

    def test_help(self): # testing argparse --help systemexit == 0 and all ok
        data = ["-h"]
        # output suppressed
        sys.stdout = io.StringIO()
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        sys.stdout = sys.__stdout__
        self.assertEqual(cm.exception.code, 0)


if __name__ == '__main__':
    unittest.main()
