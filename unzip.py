import os
import zipfile

# path of the zip file
zip_file_path = 'api-diagnostics-20230404-101458.zip'

# get the directory path of the zip file
dir_path = os.path.dirname(os.path.abspath(zip_file_path))

# change current working directory to the zip file's directory
os.chdir(dir_path)

# open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # extract all contents of the zip file
    zip_ref.extractall()
