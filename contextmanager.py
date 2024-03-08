import os
import uuid
import re


class UploaderContextManager:

    def __init__(self, file_address, temp_file_name):
        # TODO: use os.path to read the file
        self.file = open(file_address, 'r')
        self.temp_file_name = temp_file_name

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        dir_path = "temp_stories"
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        with open(f'{dir_path}/{self.temp_file_name}', 'w') as temp_file:
            temp_file.write(self.file.read())
        self.file.close()


class FilteredEditorHandle:

    def __init__(self, file_name, final_file):
        self.file_name = f'./temp_stories/{file_name}'
        self.file = open(self.file_name, 'r')
        self.new_file = None
        self.final_path = None
        self.final_file = final_file

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        pattern = r"hallo,calendar"
        txt = self.file.read()
        self.new_file = re.sub(pattern, "hello,calender", txt)
        dir_path = "final_stories"
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        with open(f'{dir_path}/{self.final_file}', 'w') as final_file:
            final_file.write(self.new_file)
        self.file.close()
        os.remove(self.file_name)
