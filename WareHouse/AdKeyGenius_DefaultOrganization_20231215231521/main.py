'''
This is the main file of the web application.
'''
from tkinter import Tk, ttk
from home_tab import HomeTab
from chat_tab import ChatTab
from history_tab import HistoryTab
from profile_tab import ProfileTab
from admin_tab import AdminTab
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("ChatDev App")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        self.home_tab = HomeTab(self.notebook)
        self.chat_tab = ChatTab(self.notebook)
        self.history_tab = HistoryTab(self.notebook)
        self.profile_tab = ProfileTab(self.notebook)
        self.admin_tab = AdminTab(self.notebook)
        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.chat_tab, text="Chat")
        self.notebook.add(self.history_tab, text="History")
        self.notebook.add(self.profile_tab, text="Profile")
        self.notebook.add(self.admin_tab, text="Admin")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = App()
    app.run()