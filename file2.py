from openpyxl import load_workbook
from sys import argv
import psycopg2
import argparse
import re
import datetime

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('excel', type=str, action='store',
                        help='path to xlsx file', nargs=1)
    if len(argv) == 1:
        print('ERROR! You must specify path to file')
        return 0
    if re.fullmatch(r'((((?<!\w)[A-Z,a-z]:)|(\.{1,2}\\))([^\b%\/\|:\n\"]'
                    r'*))|(\2([^%\/\|:\n\"]*))|((?<!\w)(\.{1,2})?(?<!\/)'
                    r'(\/((\\\b)|[^ \b%\|:\n\"\\\/])+)+\/?)', argv[1]):
        return parser
    else:
        return 0


def main():
    parser = create_parser()
    if parser is None:
        return 1
    args = parser.parse_args()
    excel = args.excel[0]
    try:
        wb = load_workbook(excel)
    except FileNotFoundError:
        print('Error FileNot Found: Enter file path carefully once more')
        return 1



    conn = psycopg2.connect(dbname='postgres', user='root',
                            password='toor', host='localhost')
    cursor = conn.cursor()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()