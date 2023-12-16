'''
This file contains the HomeTab class for the home tab of the web application.
'''
from tkinter import Frame, Label
class HomeTab(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Welcome to ChatDev App!")
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