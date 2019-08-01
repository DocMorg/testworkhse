import unittest
import project


class TestProject(unittest.TestCase):
    def test_empty1(self):  # testing if we have have not entered path to data
        result = project.create_parser(['test_data/test1.xlsx', '-c'])
        print(result)
        # self.assertEqual(result, 'Table given is empty. Enter any data and try again.')


if __name__ == '__main__':
    unittest.main()
