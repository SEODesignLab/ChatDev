'''
This file contains the AdminTab class for the admin tab of the web application.
'''
from tkinter import Frame, Label
class AdminTab(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Admin Tab")
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