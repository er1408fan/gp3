from contextmanager import UploaderContextManager
import uuid
from story import Story
from datetime import datetime


class Writer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_story(self, file_address, subject):
        temp_file_name = f'temp{uuid.uuid4().hex}.txt'
        with UploaderContextManager(file_address, temp_file_name) as f:
            pass
        Story.get_story(subject, self, datetime.now().date(), temp_file_name)


a1 = Writer("<NAME>", "<EMAIL>")
a1.add_story("test.txt")
