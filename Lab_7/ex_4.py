"""
4. Write a script that receives a directory as argument and creates a JSON file with data about all the files in that
directory. For each file, the following information will be displayed: file_name, md5_file, sha256_file, size_file
(in bytes), time when the file was created (human-readable) and the absolute path to the file.
"""
import hashlib
import json
import os
import sys


def run():
    if len(sys.argv) < 2:
        print("Run the project as following:")
        print("python.exe ex_4.py <directory-path>")
        exit()
    directory_path = sys.argv[1]
    assert os.path.isdir(directory_path), "path is not dir"
    all_files = []
    for root, directories, files in os.walk(directory_path):
        all_files += [
            os.path.abspath(os.path.join(root, file_name)) for file_name in files if
            os.path.isfile(os.path.join(root, file_name)) and os.access(os.path.join(root, file_name), os.R_OK)
        ]
    json_dict = []
    for file in all_files:
        try:
            md5_file = hashlib.md5()
            sha256_file = hashlib.sha256()
            with open(file, 'rb') as fd:
                while True:
                    data = fd.read(1024)
                    md5_file.update(data)
                    sha256_file.update(data)
                    if not data:
                        break
        except Exception as e:
            print(e)
            exit()
        json_dict.append({
            "file_name": file.split('/')[-1],
            "md5_file": md5_file.digest().decode('latin-1'),
            "sha256_file": sha256_file.digest().decode('latin-1'),
            "size_file": os.path.getsize(file),
            "time": os.path.getctime(file),
            "absolute_path": file,

        })
    with open("files_json.json", "w") as fd:
        json.dump(json_dict, fd)


if __name__ == "__main__":
    run()
