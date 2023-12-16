'''
This is the main file of the content marketing software for Direct Hearing.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
from content import Content
class ContentMarketingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Direct Hearing Content Marketing")
        self.content = Content()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to Direct Hearing Content Marketing!")
        self.label.pack()
        self.create_button = tk.Button(self.master, text="Create Content", command=self.create_content)
        self.create_button.pack()
        self.view_button = tk.Button(self.master, text="View Content", command=self.view_content)
        self.view_button.pack()
    def create_content(self):
        content_text = simpledialog.askstring("Create Content", "Enter the content:")
        if content_text:
            self.content.create(content_text)
            messagebox.showinfo("Success", "Content created successfully!")
        else:
            messagebox.showwarning("Warning", "Content cannot be empty!")
    def view_content(self):
        content_list = self.content.get_all()
        if content_list:
            messagebox.showinfo("Content List", "\n".join(content_list))
        else:
            messagebox.showinfo("Content List", "No content available.")
if __name__ == "__main__":
    root = tk.Tk()
    app = ContentMarketingApp(root)
    root.mainloop()