'''
This is the main file of the Google Ads campaign strategy app.
'''
import tkinter as tk
from tkinter import messagebox
from headline_generator import HeadlineGenerator
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Google Ads Campaign Strategy App")
        self.keyword_label = tk.Label(self, text="Enter target keyword:")
        self.keyword_label.pack()
        self.keyword_entry = tk.Entry(self)
        self.keyword_entry.pack()
        self.strategy_label = tk.Label(self, text="Select campaign strategy:")
        self.strategy_label.pack()
        self.strategy_var = tk.StringVar()
        self.strategy_var.set("Performance Max")
        self.strategy_radio1 = tk.Radiobutton(self, text="Performance Max", variable=self.strategy_var, value="Performance Max")
        self.strategy_radio1.pack()
        self.strategy_radio2 = tk.Radiobutton(self, text="Search", variable=self.strategy_var, value="Search")
        self.strategy_radio2.pack()
        self.location_label = tk.Label(self, text="Enter target location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(self)
        self.location_entry.pack()
        self.generate_button = tk.Button(self, text="Generate Headline", command=self.generate_headline)
        self.generate_button.pack()
        self.next_button = tk.Button(self, text="Next Headline", command=self.generate_next_headline)
        self.next_button.pack()
        self.headline_listbox = tk.Listbox(self, width=50, height=10)
        self.headline_listbox.pack()
        self.headlines = []
        self.current_headline_index = 0
    def generate_headline(self):
        keyword = self.keyword_entry.get()
        strategy = self.strategy_var.get()
        location = self.location_entry.get()
        if not keyword or not location:
            messagebox.showerror("Error", "Please enter a keyword and location.")
            return
        headline_generator = HeadlineGenerator()
        self.headlines = headline_generator.generate_headlines(keyword, strategy, location)
        self.current_headline_index = 0
        self.headline_listbox.delete(0, tk.END)  # Clear existing headlines
        self.headline_listbox.insert(tk.END, self.headlines[self.current_headline_index])
    def generate_next_headline(self):
        if self.current_headline_index < len(self.headlines) - 1:
            self.current_headline_index += 1
            self.headline_listbox.delete(0, tk.END)  # Clear existing headline
            self.headline_listbox.insert(tk.END, self.headlines[self.current_headline_index])
if __name__ == "__main__":
    app = App()
    app.mainloop()