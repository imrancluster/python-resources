#
# Example of ZipFile
#

import os
from zipfile import ZipFile


def main():

    # Zip example for files
    with ZipFile('new-folder.zip', 'w') as newzip:
        newzip.write('zip_testing_file2.txt')
        newzip.write('zip_testing_file1.txt')


if __name__ == '__main__':
    main()
