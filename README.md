# testworkhse

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d45f9dd08f744110862b7b8bf9a5ff90)](https://app.codacy.com/app/vlad_ustimov/testworkhse?utm_source=github.com&utm_medium=referral&utm_content=DocMorg/testworkhse&utm_campaign=Badge_Grade_Settings)

Excel to PostgreSQL transmitter written on Python 3.7

for help type in command line:
  
  $ python project.py -h

This is the test work, which purpose is to merge data from Microsoft Excel 
  (.xlsx format) data files to PostgreSQL database.
  It supports creating table with excel file on input {-c}, 
  updating it {-upd} and adding indexes {-ai}. If there is an 
  type intersection in one row during updating or creating,
  the whole row will be converted to string format.
  Names of the rows should be on the first line of the file.
  
To run the program type in command line:

$ python project.py excel.xlsx [-args]

where excel.xlsx - is the MS Excel file entry and -args -
argument you need. 
 
In the 'test.py' file are the tests made for this program.

