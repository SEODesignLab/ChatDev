'''
This is the content module for the Direct Hearing Content Marketing software.
'''
class Content:
    def __init__(self):
        self.content_list = []
    def create(self, content_text):
        self.content_list.append(content_text)
    def get_all(self):
        return self.content_list