'''
This file contains the ChatTab class for the chat tab of the web application.
'''
from tkinter import Frame, Label
class ChatTab(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Chat Tab")
        self.label.pack()
    def method1(self):
        """
        Add your implementation here.
        """
        pass
    def method2(self):
        """
        Add your implementation here.
        """
        pass