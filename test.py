import unittest
import project
import argparse
import sys
import io


class TestProject(unittest.TestCase):
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

    def test_no_args(self):  # testing with no argument argparse systemexit error == 2
        # redirect error outputs of argparse lib to nowhere, they are catched, that's ok.
        data = ["./test_data/test1.xlsx", "-dagshi"]
        sys.stderr = io.StringIO()
        data = []
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        sys.stderr = sys.__stderr__
        self.assertEqual(cm.exception.code, 2)

    def test_unexisting_args(self):
        # redirect error outputs of argparse lib to nowhere, they are catched, that's ok.
        sys.stderr = io.StringIO()
        data = []
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        sys.stderr = sys.__stderr__
        self.assertEqual(cm.exception.code, 2)

    def test_help(self):  # testing argparse --help systemexit == 0 and all ok
        data = ["-h"]
        # output suppressed
        sys.stdout = io.StringIO()
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        sys.stdout = sys.__stdout__
        self.assertEqual(cm.exception.code, 0)

    def test_file_not_found(self):  # testing invalid file exception openpyxl error
        data = ["./invalid_file.xl"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Error InvalidFileException: Enter file path carefully once more')

    def test_file_does_not_exist(self):  # testing invalid file exception found error
        data = ["./file_does_not_exist.xlsx"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Error FileNotFound: Enter file path carefully once more')

    def test_two_flags(self):
        data = ["./test_data/test1.xlsx", "-c", "-upd"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Please, select only ONE of the flag arguments: create or update')

    def test_no_action(self):
        data = ["./test_data/test1.xlsx"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'No action specified')

    def test_empty_file(self):  # testing if we have have not entered path to data
        data = ["./test_data/test1.xlsx", "-c"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Table given is empty. Enter any data and try again.')

    def test_empty_data(self):  # testing if we have have not entered path to data
        data = ["./test_data/test2.xlsx", "-c"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Table given is empty. Add some lines and try again.')

    def test_create_table(self):  # testing if we have have not entered path to data
        data = ["./test_data/test3.xlsx", "-c"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Table created successfully and filled with data')

    def test_update_table(self):  # testing if we have have not entered path to data
        data = ["./test_data/test4.xlsx", "-upd"]
        with self.assertRaises(SystemExit) as cm:
            args = self.parser.parse_args(data)
            project.main(args)
        self.assertEqual(cm.exception.code, 'Data successfully updated')


if __name__ == '__main__':
    unittest.main()
