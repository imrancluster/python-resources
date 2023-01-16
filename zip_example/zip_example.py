#
# Example of ZipFile
#

import os
from zipfile import ZipFile, ZIP_DEFLATED


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


def main():

    # Zip example for files
    with ZipFile('new-folder.zip', 'w') as newzip:
        newzip.write('zip_testing_file2.txt')
        newzip.write('zip_testing_file1.txt')

    # Zip example for folders
    with ZipFile('Python.zip', 'w', ZIP_DEFLATED) as zipf:
        zipdir('test_folder', zipf)


if __name__ == '__main__':
    main()
