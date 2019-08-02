import unittest
import project
import argparse


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

    def test_empty1(self):  # testing if we have have not entered path to data
        data = ["./test_data/test1.xlsx", "-c"]
        args = self.parser.parse_args(data)
        with self.assertRaises(SystemExit) as cm:
            project.main(args)
        the_exception = cm.exception
        self.assertEqual(the_exception.code, 'Table given is empty. Enter any data and try again.')


if __name__ == '__main__':
    unittest.main()
