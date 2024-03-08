from contextmanager import FilteredEditorHandle
import uuid


class Story:
    story_list = []

    def __init__(self, subject, author, upload_date, temp_file_name):
        self.subject = subject
        self.author = author
        self.story_checked = False
        self.upload_date = upload_date
        self.dir = None
        self.temp_file_name = temp_file_name

    def check_story(self):
        final_file = f'final{uuid.uuid4().hex}.txt'
        with FilteredEditorHandle(self.temp_file_name) as f:
            pass
        self.dir = f'final_stories/{final_file}'
        self.story_checked = True

    def stories_list(self):
        result = list(filter(lambda x: x.story_checked, self.story_list))
        return result

    @classmethod
    def get_story(cls, subject, author, upload_date, temp_file_name):
        story = cls(subject, author, upload_date, temp_file_name)
        cls.story_list.append(story)
        return story
